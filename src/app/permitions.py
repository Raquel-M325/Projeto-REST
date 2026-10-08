from rest_framework.permissions import BasePermission

class IsAvaliador(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        return request.user.tipo == "avaliador"

class IsPublicador(BasePermission):

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        return request.user.tipo == "publicador"

class CriarAvaliacaoGatewayView(APIView):

    permission_classes = [IsAvaliador]

    def post(self, request):

        # encaminhar para Interações
        ...

class CriarJogoGatewayView(APIView):

    permission_classes = [IsPublicador]

    def post(self, request):

        # encaminhar para Gerência
        ...