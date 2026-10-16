from rest_framework import serializers
from .models import PublicadorModel, PublicacaoModel, RespostaComentarioModel
from rest_framework.reverse import reverse


class PublicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicadorModel
        fields = ['id', 'nome', 'email', 'especialidade']


class PublicacaoSerializer(serializers.ModelSerializer):
    _links = serializers.SerializerMethodField()
    publicador = serializers.PrimaryKeyRelatedField(
        queryset=PublicadorModel.objects.all()
    )

    class Meta:
        model = PublicacaoModel
        fields = ['id', 'titulo', 'data_publicacao', 'publicador', 'logo', 'midia', 'descricao', '_links']

    def get__links(self, obj):
        request = self.context.get('request')
        return {
            "self": reverse('publicacao-detail', args=[obj.pk], request=request),
            "publicador": reverse('publicador-detail', args=[obj.publicador.pk], request=request)
        }


class RespostaComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespostaComentarioModel
        fields = ['id', 'id_avaliacao', 'publicacao', 'resposta_comentario', 'data_resposta']