from django.shortcuts import render, redirect
from .forms import CadastroForm, LoginForm
from django.contrib.auth import views, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def cadastro_view(request):
    form = CadastroForm(request.POST or None)

    if request.POST and form.is_valid():
        form.save()
        return redirect('base:home')

    return render(request, 'cadastro.html', locals())


def login_view(request):
    form = LoginForm(request.POST or None)

    if request.POST and form.is_valid():
        credentials = form.cleaned_data

        user = authenticate(username=credentials['cpf'], password=credentials['password'])

        if user is not None:
            login(request, user)
            return redirect('base:home')

        else:
            messages.warning(request, 'Usuário não encontrado.')
            return render(request, 'login.html', locals())

    return render(request, 'login.html', locals())


@login_required(login_url="/")
def home_view(request):
    return render(request, 'home.html')
