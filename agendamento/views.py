from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Agendamento, AgendamentoUsuario
from datetime import date, datetime


@login_required(login_url='/')
def listar_agendamentos_view(request):
    agendamentos = AgendamentoUsuario.objects.filter(usuario=request.user)

    today = date.today()
    agora = datetime.now().time()
    quantidadeHoje = AgendamentoUsuario.objects.filter(usuario=request.user, data=today, horario__gt=agora).count()
    quantidade = AgendamentoUsuario.objects.filter(usuario=request.user, data=today, horario__gt=agora).count()

    for agendamento in agendamentos:
        print(agendamento.agendamento.estabelecimento_saude)

    return render(request, 'agendamentos.html', locals())


@login_required(login_url='/')
def novo_agendamento_view(request):
    today = date.today()
    agendamentos_ativos = AgendamentoUsuario.objects.filter(Q(data__gt=today) | Q(data=today, horario__gt=datetime.now().time()))

    if agendamentos_ativos.exists():
        return redirect('agendamento:listar_agendamentos')

    return render(request, 'novo_agendamento.html')
