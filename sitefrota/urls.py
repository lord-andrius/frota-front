"""
URL configuration for sitefrota project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('motivodefeito', views.motivoDefeito, name="motivodefeito"),
    path('motivodefeito/criar', views.motivoDefeitoCriar, name="motivodefeitocriar"),
    path('motivodefeito/editar', views.motivoDefeitoEditar, name="motivodefeitoeditar"),
    path('tipoveiculo', views.tipoVeiculo, name="tipoveiculo"),
    path('tipoveiculo/criar', views.tipoVeiculoCriar, name="tipoveiculocriar"),
    path('tipoveiculo/editar', views.tipoVeiculoEditar, name="tipoveiculoeditar"),
    path('motorista', views.motorista, name="motorista"),
    path('motorista/criar', views.motoristaCriar, name="motoristacriar"),
    path('motorista/editar', views.motoristaEditar, name="motoristaeditar"),
    path('veiculo', views.veiculo, name="veiculo"),
    path('veiculo/criar', views.veiculoCriar, name="veiculocriar"),
    path('veiculo/editar', views.veiculoEditar, name="veiculoeditar"),
    path('rota', views.rota, name="rota"),
    path('rota/criar', views.rotaCriar, name="rotaCriar"),
    path('rota/editar', views.rotaEditar, name="rotaEditar"),
    path('manutencao', views.manutencao, name="manutencao"),
]
