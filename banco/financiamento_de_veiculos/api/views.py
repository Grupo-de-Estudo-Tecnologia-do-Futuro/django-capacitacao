from rest_framework import generics
from rest_framework.response import Response
from .serializers import SimulacaoVeiculoSerializer
from financiamento_de_veiculos.models import SimulacaoVeiculo

class SimulacaoVeiculoListCreate(generics.ListCreateAPIView):
    queryset = SimulacaoVeiculo.objects.all()
    serializer_class = SimulacaoVeiculoSerializer
    
