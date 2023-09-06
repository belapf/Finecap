from django.db import models

# Create your models here.

class Reserva(models.Model):
    cnpj = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    quitado = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Stand(models.Model):
    localizacao = models.CharField(max_length=200)
    valor = models.CharField(max_length=200)
    Reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)