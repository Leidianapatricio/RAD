# Prática Django - Templates e DTL (Django Template Language)

## 📋 Atividades Implementadas

### ✅ 1. Variáveis no template
- **Contexto criado em `views.py`**: passando nome de usuário (`nome_usuario`) e data atual (`now`)
- **Exibição no template**: Nome exibido em `<h1>` e data formatada com filtro `|date`
- **Arquivo**: [blog/views.py](blog/views.py) - função `home()`

### ✅ 2. Condicionais (if)
- **Flag `is_logged_in`**: 
  - Se `True`: exibe "Bem-vindo de volta!"
  - Se `False`: exibe "Faça login para continuar."
- **Campo `role`** com valores possíveis:
  - `'admin'`: Exibe mensagem de administrador com acesso total
  - `'user'`: Exibe mensagem de usuário com acesso limitado
  - Outro valor: Exibe mensagem de visitante
- **Arquivo**: [blog/templates/blog/home.html](blog/templates/blog/home.html)

### ✅ 3. Loops (for)
- **Lista de produtos**: Lista de dicionários com nome e preço
- **Exibição**: Tabela HTML com produtos usando `{% for produto in produtos %}`
- **Extras**: Uso de `{{ forloop.counter }}` para numerar linhas
- **Arquivo**: [blog/templates/blog/home.html](blog/templates/blog/home.html)

### ✅ 4. URLs (url tag)
- **Views criadas**:
  - `home`: Rota principal `/`
  - `contato`: Rota parametrizada `/contato/<telefone>/`
- **Links no template**: Usando `{% url 'nome_da_view' %}`
- **URL parametrizada**: `{% url 'contato' telefone='11999999999' %}`
- **Arquivos**: 
  - [blog/urls.py](blog/urls.py)
  - [blog/views.py](blog/views.py) - funções `home()` e `contato()`

### ✅ 5. Herança de Templates
- **Template base**: [blog/templates/blog/base.html](blog/templates/blog/base.html)
  - Possui `<header>` com navegação
  - Bloco `{% block content %}` para conteúdo
  - `<footer>` padronizado
  - Estilos CSS inclusos
- **Template filho**: [blog/templates/blog/home.html](blog/templates/blog/home.html)
  - Estende `base.html` usando `{% extends 'blog/base.html' %}`
  - Sobrescreve o bloco `content`

## 🚀 Como Testar

### 1. Iniciar o servidor Django
```bash
cd c:\Users\sheil\OneDrive\Documentos\RAD\pratica\my_project
python manage.py runserver
```

### 2. Acessar as páginas

#### Página Home (Principal)
- **URL**: http://127.0.0.1:8000/
- **Demonstra**: Variáveis, condicionais e loops

#### Página de Contato (com telefone parametrizado)
- **URL 1**: http://127.0.0.1:8000/contato/11987654321/
- **URL 2**: http://127.0.0.1:8000/contato/21987654321/
- O telefone na URL será formatado e exibido na página

### 3. Testar diferentes cenários

Para experimentar diferentes comportamentos, edite o arquivo [blog/views.py](blog/views.py), função `home()`:

```python
# Testar usuário não logado
'is_logged_in': False,  # Altere para False

# Testar diferentes perfis
'role': 'user',  # Altere para 'user' ou outro valor
```

## 📁 Estrutura de Arquivos Criados

```
blog/
├── views.py              # Views home() e contato() com contextos
├── urls.py               # Rotas configuradas
└── templates/
    └── blog/
        ├── base.html     # Template base com herança
        ├── home.html     # Template principal (herda de base.html)
        └── contato.html  # Template de contato (herda de base.html)
```

## 🎯 Conceitos DTL Aplicados

1. **Variáveis**: `{{ variavel }}`
2. **Filtros**: `{{ now|date:"d/m/Y H:i:s" }}`
3. **Tags de controle**:
   - `{% if %}...{% elif %}...{% else %}...{% endif %}`
   - `{% for %}...{% endfor %}`
4. **Herança**: `{% extends 'template.html' %}` e `{% block nome %}`
5. **URLs**: `{% url 'nome_view' parametro='valor' %}`
6. **Variáveis de loop**: `{{ forloop.counter }}`

## 💡 Observações

- O CSS está embutido no `base.html` para simplificar
- A formatação de telefone é feita na view (server-side)
- Todos os templates herdam de `base.html` para manter consistência
- A navegação está presente em todas as páginas através do header

## 📚 Referências

- Django Documentation: https://docs.djangoproject.com/
- Django Template Language: https://docs.djangoproject.com/en/stable/ref/templates/language/
