from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import SimulacaoEmprestimoSerializer
from emprestimo.models import SimulacaoEmprestimo


class SimulacaoEmprestimoCreateView(generics.ListCreateAPIView):
    serializer_class = SimulacaoEmprestimoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request':request})

        if serializer.is_valid():
            retorno_salvamento = serializer.save()
        
        return Response({
            "data": SimulacaoEmprestimoSerializer(retorno_salvamento, 
                                                  context=self.get_serializer_context()).data,
            "result": "Dados salvos com sucesso!"
        }, status=status.HTTP_201_CREATED)

# class SimularEmprestimoGet(generics.ListAPIView):
#     def get(self, resquest, *args, **kwargs):
#         try:
#             id_solicitacao = kwargs["id"]
#             emprestimo_obj = SimulacaoEmprestimo.objects.filter(id=id_solicitacao)

#             if(emprestimo_obj != None):
#                 calculo_montante = emprestimo_obj.valor_emprestimo
#             else:
#                 raise Exception ("Erro ")

#         except:
#             return Response({"error":"Resquisição não pode ser atentidada"},
#                             status= status.HTTP_400_BAD_REQUEST)