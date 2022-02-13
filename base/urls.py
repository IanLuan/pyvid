from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
]

