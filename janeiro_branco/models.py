# janeiro_branco/models.py
from django.db import models

class MensagemDeApoio(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    mensagem = models.TextField(max_length=1000)
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensagem de {self.nome}'