from rest_framework import serializers
from .models import Avaliacao, Avaliador
from gerencia.models import PublicacaoModel
from rest_framework.reverse import reverse

class AvaliadorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Avaliador
		fields = ['id', 'nome', 'especialidade']

class AvaliacaoSerializer(serializers.ModelSerializer):
	_links = serializers.SerializerMethodField()
	avaliador = serializers.PrimaryKeyRelatedField(
        	queryset=Avaliador.objects.all()
    	)
	publicacao = serializers.PrimaryKeyRelatedField(
		queryset=PublicacaoModel.objects.all(),
		allow_null=True,
		required=False,
	)
	class Meta:
		model = Avaliacao
		fields = ['id', 'nota', 'comentario', 'avaliador', 'publicacao', '_links']

	def get__links(self, obj):
		request = self.context.get('request')
		return {
			"self": reverse('avaliacao-detail', args=[obj.pk], request=request),
			"avaliador": reverse('avaliador-detail', args=[obj.avaliador.pk], request=request)
		}