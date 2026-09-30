from rest_framework import serializers
from .models import Avaliacao, Avaliador
from rest_framework.reverse import reverse

class AvaliadorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Avaliador
		fields = ['id', 'nome', 'especialidade']
