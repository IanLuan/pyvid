from django.db import models
from datetime import date, datetime


class Agendamento(models.Model):
    estabelecimento_saude = models.ForeignKey('base.EstabelecimentoSaude', on_delete=models.CASCADE)
    data = models.DateField(verbose_name='Data de agendamento')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)


class AgendamentoUsuario(models.Model):
    agendamento = models.ForeignKey('Agendamento', on_delete=models.CASCADE)
    usuario = models.ForeignKey('base.Usuario', on_delete=models.CASCADE)
    data = models.DateField(verbose_name='Data de agendamento')
    horario = models.TimeField(verbose_name='Horário de agendamento')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    @property
    def status(self):
        if self.data < date.today():
            return 'Expirado'
        elif self.data == date.today():
            if self.horario < datetime.now().time():
                return 'Expirado'
            else:
                return 'Agendado'
        else:
            return 'Agendado'
