from rest_framework import serializers
from financiamento_imovel.models import FinanciamentoImovel

class FinanciamentoImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanciamentoImovel
        fields = '__all__'