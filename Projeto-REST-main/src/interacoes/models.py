from django.db import models
from django.contrib.auth.models import User
from gerencia.models import PublicacaoModel

# Create your models here.

class Avaliador(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil_avaliador",
        null=True,
        blank=True,
    )
    nome = models.CharField(max_length = 255, blank = False, null=False)
    especialidade = models.CharField(max_length = 255, blank = False, null=False)

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    nota = models.IntegerField(blank = False, null=False)
    #like = models.BooleanField(default None)
    comentario = models.CharField(max_length = 500)
    data_critica = models.DateField(auto_now=True)
    avaliador = models.ForeignKey(Avaliador, related_name = "avaliacao", on_delete = models.CASCADE)
    publicacao = models.ForeignKey(
        PublicacaoModel,
        related_name="avaliacoes",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.comentario