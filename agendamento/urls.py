from django.urls import path
from . import views

app_name = 'agendamento'

urlpatterns = [
    path('', views.listar_agendamentos_view, name='listar_agendamentos'),
    path('novo/', views.novo_agendamento_view, name='novo_agendamento')
]