from django.urls import path

urlspatterns =[
    path("financiamento_imovel/", FinanciamentoImovelListCreateView.as_view()),
]