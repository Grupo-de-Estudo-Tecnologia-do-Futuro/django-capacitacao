from django.db import models

class SimulacaoEmprestimo(models.Model):
    id= models.CharField(primary_key=True, max_length=10)
    valor_veiculos = models.FloatField(max_digits=2, decimal_places=2)
    entrada_veiculos = models.FloatField(max_digits=2, decimal_places= 2)
    prazo_financiamento = models.IntegerField()
