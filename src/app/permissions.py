from rest_framework.permissions import BasePermission, SAFE_METHODS


def tipo_usuario(request):
    token = request.auth

    if token is None:
        return None

    return token.get("tipo")


class IsAvaliador(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and tipo_usuario(request) == "avaliador"
        )


class IsPublicador(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and tipo_usuario(request) == "publicador"
        )


class LeituraAutenticadaEscritaAvaliador(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        tipo = tipo_usuario(request)

        if request.method in SAFE_METHODS:
            return tipo in ("avaliador", "publicador")

        return tipo == "avaliador"


class LeituraAutenticadaEscritaPublicador(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        tipo = tipo_usuario(request)

        if request.method in SAFE_METHODS:
            return tipo in ("avaliador", "publicador")

        return tipo == "publicador"