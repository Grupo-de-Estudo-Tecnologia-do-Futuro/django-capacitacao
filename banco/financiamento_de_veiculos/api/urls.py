from django.urls import path
from .views import SimulacaoVeiculoListCreate

urlpatterns = [
    path("financiamento_veiculo/", SimulacaoVeiculoListCreate.as_view()),
]
