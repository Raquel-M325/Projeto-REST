from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PublicacaoModel, PublicadorModel, RespostaComentarioModel
from .serializers import PublicacaoSerializer, PublicadorSerializer, RespostaComentarioSerializer

from rest_framework import viewsets, permissions


class PublicadorViewSet(viewsets.ModelViewSet):
    queryset = PublicadorModel.objects.all()

    serializer_class = PublicadorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PublicacaoViewSet(viewsets.ModelViewSet):
    queryset = PublicacaoModel.objects.all()

    serializer_class = PublicacaoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = PublicacaoModel.objects.all()

        publicador_id = self.request.query_params.get('publicador')
        titulo = self.request.query_params.get('titulo')

        if publicador_id:
            try:
                publicador_id = int(publicador_id)
                queryset = queryset.filter(publicador_id=publicador_id)
            except ValueError:
                return Response(
                    {"erro": "O ID do publicador deve ser um número válido"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)

        return queryset

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)