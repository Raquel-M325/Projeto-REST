from rest_framework.permissions import BasePermission, SAFE_METHODS


def tipo_usuario(request):
    token = request.auth
    if token is None:
        return None
    try:
        return token.get("tipo")
    except AttributeError:
        return None


class IsAvaliador(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated) and tipo_usuario(request) == "avaliador"


class IsPublicador(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated) and tipo_usuario(request) == "publicador"


class LeituraAutenticadaEscritaAvaliador(BasePermission):
    """Leitura para avaliadores/publicadores; escrita apenas para avaliadores."""
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        tipo = tipo_usuario(request)
        if request.method in SAFE_METHODS:
            return tipo in ("avaliador", "publicador")
        return tipo == "avaliador"


class LeituraAutenticadaEscritaPublicador(BasePermission):
    """Leitura para avaliadores/publicadores; escrita apenas para publicadores."""
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        tipo = tipo_usuario(request)
        if request.method in SAFE_METHODS:
            return tipo in ("avaliador", "publicador")
        return tipo == "publicador"


class InternalGatewayOnly(BasePermission):
    """Impede o uso direto dos endpoints internos sem passar pelo gateway."""
    def has_permission(self, request, view):
        from django.conf import settings
        expected = getattr(settings, "GATEWAY_INTERNAL_TOKEN", "")
        supplied = request.headers.get("X-Gateway-Internal", "")
        return bool(expected) and supplied == expected
