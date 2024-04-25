from django.db import models

class FinanciamentoVeiculos(models.Model):
    id= models.CharField(primary_key=True, max_length=10)
    valor_veiculos = models.DecimalField(max_digits=10, decimal_places=2)
    entrada_veiculos = models.DecimalField(max_digits=5, decimal_places= 2)
    prazo_financiamento = models.IntegerField()
