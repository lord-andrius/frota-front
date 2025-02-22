from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def motorista(request):
    template = loader.get_template('motorista.html')
    return HttpResponse(template.render())

def motoristaCriar(request):
    template = loader.get_template('motoristacriar.html')
    return HttpResponse(template.render())

def motoristaEditar(request):
    template = loader.get_template('motoristaeditar.html')
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

def tipoVeiculo(request):
    template = loader.get_template('tipoveiculo.html')
    return HttpResponse(template.render())

def tipoVeiculoCriar(request):
    template = loader.get_template('tipoveiculocriar.html')
    return HttpResponse(template.render())

def tipoVeiculoEditar(request):
    template = loader.get_template('tipoveiculoeditar.html')
    return HttpResponse(template.render())

def veiculo(request):
    template = loader.get_template('veiculo.html')
    return HttpResponse(template.render())

def veiculoCriar(request):
    template = loader.get_template('veiculocriar.html')
    return HttpResponse(template.render())

def veiculoEditar(request):
    template = loader.get_template('veiculoeditar.html')
    return HttpResponse(template.render())

def rota(request):
    template = loader.get_template('rota.html')
    return HttpResponse(template.render())

def manutencao(request):
    template = loader.get_template('manutencao.html')
    return HttpResponse(template.render()) 