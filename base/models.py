from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from localflavor.br.validators import BRCPFValidator
from localflavor.br.models import BRCPFField
from datetime import date


class UserManager(BaseUserManager):

    def _create_user(self, cpf, password, **extra_fields):

        if not cpf:
            raise ValueError("O CPF é obrigatório")

        cpf_validator = BRCPFValidator()
        cpf_validator(cpf)

        user = self.model(cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'cpf'

    cpf = BRCPFField(verbose_name='CPF', primary_key=True)
    nome = models.CharField(verbose_name='Nome completo', max_length=255)
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = UserManager()

    @property
    def idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))


class EstabelecimentoSaude(models.Model):
    cnes = models.CharField(db_column='CO_CNES', max_length=7, unique=True, verbose_name='CNES')
    nome_fantasia = models.CharField(max_length=255)

    criado_em = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Atualizado em')

    def __str__(self):
        return self.cnes + ' - ' + self.nome_fantasia
