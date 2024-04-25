from django.urls import path
from .views import FinanciamentoVeiculoListCreateView

urlpatterns = [
path("financiamento_veiculos/", FinanciamentoVeiculoListCreateView.as_view()),

]