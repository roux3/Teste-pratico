from pyexpat import model
from sys import maxsize
from django.db import models
from matplotlib.pyplot import text
from django.core.validators import MaxValueValidator

class Endereco(models.Model):
    cep = models.IntegerField(null=True,blank=True,validators=[MaxValueValidator(99999999)])
    endereco = models.TextField()
    numero = models.IntegerField(validators=[MaxValueValidator(99999)])
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf= models.CharField(max_length=2)
    descricao = models.TextField()

    def __str__(self):
        return str(self.cep)

# Create your models here.
