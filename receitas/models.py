from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

class Receita(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete = models.DO_NOTHING)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.CharField(max_length=300)
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    modo_preparo = models.TextField()
    foto_1 = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    foto_2 = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    foto_3 = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=True)
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.nome_receita
