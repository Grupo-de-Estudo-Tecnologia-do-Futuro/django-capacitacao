from rest_framework import generics
from rest_framework.response import Response
from .serializers import FinanciamentoVeiculosSerializer
from financiamento_veiculos.models import FinanciamentoVeiculos



class FinanciamentoVeiculolListCreateView(generics.ListCreateAPIView):
    queryset = FinanciamentoVeiculos.objects.all()
    serializer_class =  FinanciamentoVeiculosSerializer