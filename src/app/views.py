# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .services.gerencia import listar_publicacoes
from .services.interacoes import listar_avaliacoes


class PublicacaoGatewayView(APIView):

    def get(self, request):

        token = request.auth

        response = listar_publicacoes(token)

        return Response(
            response.json(),
            status=response.status_code
        )


class AvaliacaoGatewayView(APIView):

    def get(self, request):

        token = request.auth

        response = listar_avaliacoes(token)

        return Response(
            response.json(),
            status=response.status_code
        )