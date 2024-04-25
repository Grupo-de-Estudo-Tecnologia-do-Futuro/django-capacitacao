from django.urls import path
from .views import FinanciamentoVeiculolListCreateView

urlpatterns = [
path("financiamento_veiculos/", FinanciamentoVeiculolListCreateView.as_view()),

]