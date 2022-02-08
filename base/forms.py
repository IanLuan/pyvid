from django.contrib.auth.forms import UserCreationForm
from django import forms
from localflavor.br.forms import BRCPFField

from base.models import Usuario


class CadastroForm(UserCreationForm):
    cpf = BRCPFField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = ("nome", "cpf", "data_nascimento", "password1", "password2")


class LoginForm(forms.Form):
    cpf = BRCPFField()
    password = forms.CharField(widget=forms.PasswordInput())

