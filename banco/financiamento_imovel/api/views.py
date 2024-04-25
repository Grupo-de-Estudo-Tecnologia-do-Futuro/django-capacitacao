from rest_framework import generics
from rest_framework.response import Response
from .serializers import FinanciamentoImovelSerializer
from financiamento_imovel.models import FinanciamentoImovel

class FinanciamentoImovelListCreate(generics.ListAPIView):
    queryset = FinanciamentoImovel.objects.all()
    serializer_class = FinanciamentoImovelSerializer
    
