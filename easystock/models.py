from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.FloatField(max_length=255)
    
    def __str__(self):
        return self.nome
    
class Tipo(models.Model):
    departamentos = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao
    
class Classificacoe(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
