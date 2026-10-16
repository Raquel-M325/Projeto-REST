from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model


class TipoTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get("username")
        User = get_user_model()
        user = User.objects.filter(email__iexact=username).first()
        if user:
            attrs["username"] = user.get_username()
        try:
            data = super().validate(attrs)
        except AuthenticationFailed:
            raise AuthenticationFailed("Usuário/e-mail ou senha incorreto(s)")
        token = self.get_token(self.user)
        data["tipo"] = token.get("tipo")
        data["nome"] = token.get("nome")
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        if hasattr(user, "perfil_avaliador"):
            token["tipo"] = "avaliador"
            token["nome"] = user.perfil_avaliador.nome
        elif hasattr(user, "perfil_publicador"):
            token["tipo"] = "publicador"
            token["nome"] = user.perfil_publicador.nome
        else:
            token["tipo"] = "admin"
            token["nome"] = user.get_full_name() or user.username
        return token