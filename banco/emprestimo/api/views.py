from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import SimulacaoEmprestimoSerializer


class SimulacaoEmprestimoCreateView(generics.ListCreateAPIView):
    serializer_class = SimulacaoEmprestimoSerializer

    def post (self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context=({'request':request}))

        if serializer.is_valid():
            retorno_salvadmento = serializer.save()

            return Response(
                {"data": SimulacaoEmprestimoSerializer(retorno_salvadmento,
                                                      context=self.get_serializer_context()).data,
                "result": "Dados salvos"
                
            }, status = status.HTTP_201_CREATED)