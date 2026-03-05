from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def welcome(request):
    return HttpResponse('Bem-vindo ao meu blog!')

def eco(request, texto):
    return HttpResponse(f'Você digitou: {texto}')

def info(request):
    dados = {
        "disciplina": "RAD",
        "framework": "Django",
        "semestre": "2026.1"
    }
    return JsonResponse(dados)
