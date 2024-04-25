from rest_framework import serializers
from financiamento_veiculos.models import FinanciamentoVeiculos


class FinanciamentoVeiculosSerializer(serializers.ModelSerializer):
    class Meta:

        model = FinanciamentoVeiculos
        fields = '__all__'