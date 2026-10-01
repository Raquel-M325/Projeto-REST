from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

	def get_queryset(self):
		queryset = Avaliacao.objects.all()
		comentario = self.request.query_params.get('comentario')

		nota = self.request.query_params.get('nota')

		if comentario:
			queryset = queryset.filter(comentario__icontains = comentario)
		if nota:
			queryset = queryset.filter(nota = nota)
		return queryset

	def create(self, request, *args, **kwargs):
		print(request.data)
		return super().create(request, *args, **kwargs)

class AvaliacaoListView(APIView):
	def get(self, request):
		avaliador_id = request.query_params.get('avaliador')
		avaliacoes = Avaliacao.objects.all()
		
		if avaliador_id:
			try:
				avaliacoes = avaliacoes.filter(avaliador_id=int(avaliador_id))
			except ValueError:
			
				return Response(
					{"erro": "ID do avaliador deve ser um número válido"},
					status=status.HTTP_400_BAD_REQUEST
				)
		
		serializer = AvaliacaoSerializer(avaliacoes, many=True)
		return Response(serializer.data)