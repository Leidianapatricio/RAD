from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime

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

# Prática Django DTL

def home(request):
    """
    View principal que demonstra:
    1. Variáveis no template (nome_usuario, now)
    2. Condicionais (is_logged_in, role)
    3. Loops (produtos)
    """
    contexto = {
        # 1. Variáveis
        'nome_usuario': 'Leidiana',
        'now': datetime.now(),
        
        # 2. Condicionais
        'is_logged_in': True,  # Altere para False para testar
        'role': 'admin',  # Valores possíveis: 'admin', 'user', ou qualquer outro
        
        # 3. Loop - Lista de produtos
        'produtos': [
            {'nome': 'Notebook Dell', 'preco': '3.500,00'},
            {'nome': 'Mouse Logitech', 'preco': '150,00'},
            {'nome': 'Teclado Mecânico', 'preco': '450,00'},
            {'nome': 'Monitor LG 24"', 'preco': '800,00'},
            {'nome': 'Webcam Full HD', 'preco': '250,00'},
        ]
    }
    return render(request, 'blog/home.html', contexto)

def contato(request, telefone):
    """
    View de contato com URL parametrizada
    O telefone é recebido como parâmetro da URL
    """
    # Formata o telefone para exibição
    telefone_formatado = telefone
    if len(telefone) == 11:
        # Formato: (XX) XXXXX-XXXX
        telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    elif len(telefone) == 10:
        # Formato: (XX) XXXX-XXXX
        telefone_formatado = f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
    
    contexto = {
        'telefone_formatado': telefone_formatado,
    }
    return render(request, 'blog/contato.html', contexto)
