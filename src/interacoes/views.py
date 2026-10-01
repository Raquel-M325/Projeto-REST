from django.shortcuts import render
from .models import Avaliacao, Avaliador
from .serializers import AvaliadorSerializer, AvaliacaoSerializer

from rest_framework import viewsets, permissions
# Create your views here.

class AvaliadorViewSet(viewsets.ModelViewSet):
	queryset = Avaliador.objects.all()

	serializer_class = AvaliadorSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AvaliacaoViewSet(viewsets.ModelViewSet):
	queryset = Avaliacao.objects.all()

	serializer_class = AvaliacaoSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]