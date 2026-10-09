
from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .service import ClienteService


class ClienteViewSet(viewsets.ViewSet):

    def _requisicao_gateway(self, request, metodo, endpoint):
        token = request.headers.get("Authorization")

        resultado = ClienteService.requisicao(
            metodo=metodo,
            endpoint=endpoint,
            token=token,
            dados=request.data if metodo in ("POST", "PUT", "PATCH") else None,
            arquivos=request.FILES or None,
        )

        return Response(
            resultado["dados"],
            status=resultado["status"],
        )

    # PUBLICADORES

    def listar_publicadores(self, request):
        return self._requisicao_gateway(
            request, "GET", "/api/publicador/"
        )

    def criar_publicador(self, request):
        return self._requisicao_gateway(
            request, "POST", "/api/publicador/"
        )

    def detalhar_publicador(self, request, pk=None):
        return self._requisicao_gateway(
            request, "GET", f"/api/publicador/{pk}/"
        )

    def editar_publicador(self, request, pk=None):
        return self._requisicao_gateway(
            request, "PUT", f"/api/publicador/{pk}/"
        )

    def atualizar_parcial_publicador(self, request, pk=None):
        return self._requisicao_gateway(
            request, "PATCH", f"/api/publicador/{pk}/"
        )

    def excluir_publicador(self, request, pk=None):
        return self._requisicao_gateway(
            request, "DELETE", f"/api/publicador/{pk}/"
        )


    # PUBLICAÇÕES

    def listar_publicacoes(self, request):
        return self._requisicao_gateway(
            request, "GET", "/api/publicacao/"
        )

    @swagger_auto_schema(
        operation_description="Cria uma nova publicação.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['titulo', 'data_publicacao', 'publicador'],
            properties={
                'titulo': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Título da publicação'
                ),
                'data_publicacao': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    format='date',
                    description='Data da publicação (AAAA-MM-DD)'
                ),
                'publicador': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='ID do publicador existente'
                ),
            }
        ),
    )
    def criar_publicacao(self, request):
        return self._requisicao_gateway(
            request, "POST", "/api/publicacao/"
        )

    
    def detalhar_publicacao(self, request, pk=None):
        return self._requisicao_gateway(
            request, "GET", f"/api/publicacao/{pk}/"
        )

    def editar_publicacao(self, request, pk=None):
        return self._requisicao_gateway(
            request, "PUT", f"/api/publicacao/{pk}/"
        )

    def atualizar_parcial_publicacao(self, request, pk=None):
        return self._requisicao_gateway(
            request, "PATCH", f"/api/publicacao/{pk}/"
        )

    def excluir_publicacao(self, request, pk=None):
        return self._requisicao_gateway(
            request, "DELETE", f"/api/publicacao/{pk}/"
        )

    # AVALIADORES

    def listar_avaliadores(self, request):
        return self._requisicao_gateway(
            request, "GET", "/api/avaliador/"
        )

    def criar_avaliador(self, request):
        return self._requisicao_gateway(
            request, "POST", "/api/avaliador/"
        )

    def detalhar_avaliador(self, request, pk=None):
        return self._requisicao_gateway(
            request, "GET", f"/api/avaliador/{pk}/"
        )

    def editar_avaliador(self, request, pk=None):
        return self._requisicao_gateway(
            request, "PUT", f"/api/avaliador/{pk}/"
        )

    def atualizar_parcial_avaliador(self, request, pk=None):
        return self._requisicao_gateway(
            request, "PATCH", f"/api/avaliador/{pk}/"
        )

    def excluir_avaliador(self, request, pk=None):
        return self._requisicao_gateway(
            request, "DELETE", f"/api/avaliador/{pk}/"
        )

    # AVALIAÇÕES

    def listar_avaliacoes(self, request):
        return self._requisicao_gateway(
            request, "GET", "/api/avaliacao/"
        )

    def criar_avaliacao(self, request):
        return self._requisicao_gateway(
            request, "POST", "/api/avaliacao/"
        )

    def detalhar_avaliacao(self, request, pk=None):
        return self._requisicao_gateway(
            request, "GET", f"/api/avaliacao/{pk}/"
        )

    def editar_avaliacao(self, request, pk=None):
        return self._requisicao_gateway(
            request, "PUT", f"/api/avaliacao/{pk}/"
        )

    def atualizar_parcial_avaliacao(self, request, pk=None):
        return self._requisicao_gateway(
            request, "PATCH", f"/api/avaliacao/{pk}/"
        )

    def excluir_avaliacao(self, request, pk=None):
        return self._requisicao_gateway(
            request, "DELETE", f"/api/avaliacao/{pk}/"
        )