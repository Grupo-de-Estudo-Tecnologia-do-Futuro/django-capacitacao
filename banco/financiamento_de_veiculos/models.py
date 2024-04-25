from django.db import models

class SimulacaoVeiculo(models.Model):
    id = models.CharField(primary_key=True, max_length=10) # editable = Flase and UUID.
    valor_veiculo = models.DecimalField(max_digits=10, decimal_places=2)
    valor_entrada = models.DecimalField(max_digits=5, decimal_places=2)
    prazo_financiamento = models.IntegerField()
