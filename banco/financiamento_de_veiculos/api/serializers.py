from rest_framework import serializers
from financiamento_de_veiculos.models import SimulacaoVeiculo


class SimulacaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimulacaoVeiculo
        fields = '__all__'