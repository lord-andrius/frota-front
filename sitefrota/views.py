from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def motorista(request):
    template = loader.get_template('motorista.html')
    return HttpResponse(template.render())

def motivoDefeito(request):
    template = loader.get_template('motivodefeito.html')
    return HttpResponse(template.render())

def motivoDefeitoCriar(request):
    template = loader.get_template('motivodefeitocriar.html')
    return HttpResponse(template.render())

def motivoDefeitoEditar(request):
    template = loader.get_template('motivodefeitoeditar.html')
    return HttpResponse(template.render())

def veiculo(request):
    template = loader.get_template('veiculo.html')
    return HttpResponse(template.render())

def rota(request):
    template = loader.get_template('rota.html')
    return HttpResponse(template.render())

def manutencao(request):
    template = loader.get_template('manutencao.html')
    return HttpResponse(template.render()) 