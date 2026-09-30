from django.shortcuts import render
from models import Avaliacao, Avaliador

from rest_framework import viewsets, permissions
# Create your views here.

class Teste(viewsets.ModelsViewSet):
    def get(self, request):  # metodo get pq o django negou o acesso da aplicação
        avaliacoes = ListarProjetosMaisAvaliadosService.executar(3)  # top 3 projetos mais avaliados

        return render(request, "templates/index.html")
    # queryset = Autor.objects.all()

	# serializer_class = AutorSerializer
	# permission_classes = [permissions.IsAuthenticatedOrReadOnly]