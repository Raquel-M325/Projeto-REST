from django.db import models
# from .models import Usuario

# Create your models here.

class Avaliador(models.Model):
    nome = models.CharField(max_length = 255)
    especialidade = models.CharField(max_length = 255)

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    nota = models.IntegerField()
    #like = models.BooleanField(default None)
    comentario = models.CharField(max_length = 500)
    data_critica = models.DateField(auto_now=True)
    avaliador = models.ForeignKey(Avaliador, related_name = "avaliacao", on_delete = models.CASCADE)

    def __str__(self):
        return comentario