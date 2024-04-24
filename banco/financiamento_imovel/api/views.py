from rest_framework import generics
from rest_framework.response import response
from .serializers import FinanciamentoImovelSerializer
from financiamento_imovel.models import FinanciamentoImovel

class FinanciamentoImovelListCreateView(generics.ListCreateAPIView):
    queryset = FinanciamentoImovel.objects.all()
    serializer_class =  FinanciamentoImovelSerializer

