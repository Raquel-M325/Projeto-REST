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
    """
    Leitura: avaliadores e publicadores.
    Escrita: somente avaliadores.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        tipo = tipo_usuario(request)

        if request.method in SAFE_METHODS:
            return tipo in ("avaliador", "publicador")

        return tipo == "avaliador"


class LeituraAutenticadaEscritaPublicador(BasePermission):
    """
    Leitura: avaliadores e publicadores.
    Escrita: somente publicadores.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        tipo = tipo_usuario(request)

        if request.method in SAFE_METHODS:
            return tipo in ("avaliador", "publicador")

        return tipo == "publicador"

# class CriarAvaliacaoGatewayView(APIView):

#     permission_classes = [IsAvaliador]

#     def post(self, request):

#         # encaminhar para Interações
#         if (permission_classes == "publicador"):

#         ...

# class CriarJogoGatewayView(APIView):

#     permission_classes = [IsPublicador]

#     def post(self, request):

#         # encaminhar para Gerência
#         ...