from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

from gerencia.models import PublicadorModel
from interacoes.models import Avaliador


User = get_user_model()


class CadastroBaseSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    nome = serializers.CharField(max_length=255)
    especialidade = serializers.CharField(max_length=255)

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("Este nome de usuário já está em uso.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Este e-mail já está em uso.")
        return value


class CadastroAvaliadorSerializer(CadastroBaseSerializer):
    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(
                username=validated_data["username"],
                email=validated_data["email"],
                password=validated_data["password"],
            )
            perfil = Avaliador.objects.create(
                usuario=user,
                nome=validated_data["nome"],
                especialidade=validated_data["especialidade"],
            )
        return user, perfil


class CadastroPublicadorSerializer(CadastroBaseSerializer):
    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(
                username=validated_data["username"],
                email=validated_data["email"],
                password=validated_data["password"],
            )
            perfil = PublicadorModel.objects.create(
                usuario=user,
                nome=validated_data["nome"],
                email=validated_data["email"],
                especialidade=validated_data["especialidade"],
            )
        return user, perfil
