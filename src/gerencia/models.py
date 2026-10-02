from django.db import models


# Create your models here.

class PublicadorModel(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    especialidade = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nome


class PublicacaoModel(models.Model):
    titulo = models.CharField(max_length=255, null=False, blank=False)
    data_publicacao = models.DateField(null=False, blank=False)
    publicador = models.ForeignKey(PublicadorModel, on_delete=models.CASCADE, related_name='publicacoes')
    logo = models.ImageField(upload_to='imagens/', null=True, blank=True)
    midia = models.FileField(upload_to='midias/', null=True, blank=True)
    descricao = models.TextField(max_length=500, null=True, blank=True)
    
   
    def __str__(self):
        return self.titulo


class RespostaComentarioModel(models.Model):
    id_avaliacao = models.IntegerField()  
    publicacao = models.ForeignKey(PublicacaoModel, on_delete=models.CASCADE, related_name='respostas_comentarios')
    resposta_comentario = models.TextField(max_length=500, null=True, blank=True)
    data_resposta = models.DateField(auto_now=True)

    def __str__(self):
        return self.resposta_comentario or "Sem resposta"