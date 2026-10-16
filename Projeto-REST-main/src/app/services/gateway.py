import requests
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Avg, Count
from interacoes.models import Avaliacao


RESOURCE_CONFIG = {
    "publicadores": ("publicador", "publicador"),
    "publicacoes": ("publicacao", "publicador"),
    "avaliadores": ("avaliador", "avaliador"),
    "avaliacoes": ("avaliacao", "avaliador"),
}


class NotasPublicasView(APIView):
    """Expõe somente indicadores agregados de nota, sem comentários/identidade."""
    permission_classes = [AllowAny]

    def get(self, request):
        resumo = (
            Avaliacao.objects.filter(publicacao__isnull=False)
            .values("publicacao_id")
            .annotate(nota_media=Avg("nota"), total_avaliacoes=Count("id"))
            .order_by("publicacao_id")
        )
        return Response(list(resumo))


class GatewayProxyView(APIView):
    """
    API Gateway: valida JWT/perfil, escolhe o serviço interno e encaminha
    método, filtros, corpo e arquivos. Os endpoints internos exigem segredo.
    """
    permission_classes = [IsAuthenticated]

    def _perfil_permitido(self, request, recurso, metodo):
        tipo = request.auth.get("tipo") if request.auth else None
        recurso_interno, perfil_escrita = RESOURCE_CONFIG[recurso]
        if metodo in ("GET", "HEAD", "OPTIONS"):
            return tipo in ("avaliador", "publicador")
        return tipo == perfil_escrita

    def dispatch(self, request, *args, **kwargs):
        # Keep DRF's normal dispatch/authentication behavior.
        return super().dispatch(request, *args, **kwargs)

    def handle(self, request, recurso, pk=None):
        if recurso not in RESOURCE_CONFIG:
            return Response({"detail": "Recurso não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        if not self._perfil_permitido(request, recurso, request.method):
            return Response(
                {"detail": "Você não tem permissão para realizar esta operação."},
                status=status.HTTP_403_FORBIDDEN,
            )

        recurso_interno, _perfil_escrita = RESOURCE_CONFIG[recurso]
        base_url = getattr(settings, "GATEWAY_INTERNAL_URL", "http://127.0.0.1:8000")
        endpoint = f"/__internal__/{recurso_interno}/"
        if pk is not None:
            endpoint += f"{pk}/"

        headers = {"X-Gateway-Internal": settings.GATEWAY_INTERNAL_TOKEN}
        auth_header = request.headers.get("Authorization")
        if auth_header:
            headers["Authorization"] = auth_header

        params = request.query_params
        files = None
        data = None
        json_data = None
        if request.method in ("POST", "PUT", "PATCH"):
            if request.FILES:
                data = request.data.copy()
                files = []
                for field, uploaded in request.FILES.items():
                    files.append((field, (uploaded.name, uploaded.file, uploaded.content_type)))
            else:
                json_data = request.data

        try:
            upstream = requests.request(
                method=request.method,
                url=f"{base_url.rstrip('/')}{endpoint}",
                headers=headers,
                params=params,
                json=json_data,
                data=data,
                files=files,
                timeout=10,
            )
        except requests.Timeout:
            return Response({"detail": "Tempo limite ao acessar o serviço interno."},
                            status=status.HTTP_504_GATEWAY_TIMEOUT)
        except requests.RequestException:
            return Response({"detail": "Não foi possível acessar o serviço interno."},
                            status=status.HTTP_502_BAD_GATEWAY)

        if upstream.status_code == 204 or not upstream.content:
            return Response(status=upstream.status_code)
        try:
            payload = upstream.json()
        except ValueError:
            payload = {"detail": upstream.text}

        # Serializer links internos devem apontar para a API pública do gateway.
        substitutions = {
            "/__internal__/publicador/": "/api/v1/publicadores/",
            "/__internal__/publicacao/": "/api/v1/publicacoes/",
            "/__internal__/avaliador/": "/api/v1/avaliadores/",
            "/__internal__/avaliacao/": "/api/v1/avaliacoes/",
        }
        def rewrite_links(value):
            if isinstance(value, dict):
                return {key: rewrite_links(item) for key, item in value.items()}
            if isinstance(value, list):
                return [rewrite_links(item) for item in value]
            if isinstance(value, str):
                for old, new in substitutions.items():
                    value = value.replace(old, new)
            return value

        return Response(rewrite_links(payload), status=upstream.status_code)

    def get(self, request, recurso, pk=None): return self.handle(request, recurso, pk)
    def post(self, request, recurso, pk=None): return self.handle(request, recurso, pk)
    def put(self, request, recurso, pk=None): return self.handle(request, recurso, pk)
    def patch(self, request, recurso, pk=None): return self.handle(request, recurso, pk)
    def delete(self, request, recurso, pk=None): return self.handle(request, recurso, pk)
    def head(self, request, recurso, pk=None): return self.handle(request, recurso, pk)
