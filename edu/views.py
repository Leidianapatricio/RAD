from django.shortcuts import get_object_or_404, redirect, render

from .forms import AutorForm, EditoraForm, LivroForm, PublicaForm
from .models import Autor, Editora, Livro, Publica


def index(request):
    return render(request, 'edu/index.html')


def _render_list(request, title, object_label, create_url, rows, headers):
    return render(request, 'edu/list.html', {
        'title': title,
        'object_label': object_label,
        'create_url': create_url,
        'rows': rows,
        'headers': headers,
    })


def autor_list(request):
    autores = Autor.objects.all()
    rows = [
        {
            'id': autor.id,
            'fields': [autor.id, autor.nome],
            'edit_url': 'edu:autor_update',
            'delete_url': 'edu:autor_delete',
        }
        for autor in autores
    ]
    return _render_list(request, 'Autores', 'autor', 'edu:autor_create', rows, ['ID', 'Nome'])


def autor_create(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('edu:autor_list')
    return render(request, 'edu/form.html', {'title': 'Novo autor', 'form': form})


def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    form = AutorForm(request.POST or None, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('edu:autor_list')
    return render(request, 'edu/form.html', {'title': 'Editar autor', 'form': form})


def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('edu:autor_list')
    return render(request, 'edu/delete.html', {'title': 'Excluir autor', 'object': autor, 'cancel_url': 'edu:autor_list'})


def editora_list(request):
    editoras = Editora.objects.all()
    rows = [
        {
            'id': editora.id,
            'fields': [editora.id, editora.nome],
            'edit_url': 'edu:editora_update',
            'delete_url': 'edu:editora_delete',
        }
        for editora in editoras
    ]
    return _render_list(request, 'Editoras', 'editora', 'edu:editora_create', rows, ['ID', 'Nome'])


def editora_create(request):
    form = EditoraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('edu:editora_list')
    return render(request, 'edu/form.html', {'title': 'Nova editora', 'form': form})


def editora_update(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    form = EditoraForm(request.POST or None, instance=editora)
    if form.is_valid():
        form.save()
        return redirect('edu:editora_list')
    return render(request, 'edu/form.html', {'title': 'Editar editora', 'form': form})


def editora_delete(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == 'POST':
        editora.delete()
        return redirect('edu:editora_list')
    return render(request, 'edu/delete.html', {'title': 'Excluir editora', 'object': editora, 'cancel_url': 'edu:editora_list'})


def livro_list(request):
    livros = Livro.objects.select_related('editora').all()
    rows = [
        {
            'id': livro.id,
            'fields': [livro.id, livro.isbn, livro.titulo, livro.publicacao, livro.preco, livro.estoque, livro.editora.nome],
            'edit_url': 'edu:livro_update',
            'delete_url': 'edu:livro_delete',
        }
        for livro in livros
    ]
    return _render_list(request, 'Livros', 'livro', 'edu:livro_create', rows, ['ID', 'ISBN', 'Título', 'Publicação', 'Preço', 'Estoque', 'Editora'])


def livro_create(request):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('edu:livro_list')
    return render(request, 'edu/form.html', {'title': 'Novo livro', 'form': form})


def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    form = LivroForm(request.POST or None, instance=livro)
    if form.is_valid():
        form.save()
        return redirect('edu:livro_list')
    return render(request, 'edu/form.html', {'title': 'Editar livro', 'form': form})


def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('edu:livro_list')
    return render(request, 'edu/delete.html', {'title': 'Excluir livro', 'object': livro, 'cancel_url': 'edu:livro_list'})


def publica_list(request):
    publicacoes = Publica.objects.select_related('autor', 'livro').all()
    rows = [
        {
            'id': publica.id,
            'fields': [publica.id, publica.autor.nome, publica.livro.titulo, publica.livro.isbn],
            'edit_url': 'edu:publica_update',
            'delete_url': 'edu:publica_delete',
        }
        for publica in publicacoes
    ]
    return _render_list(request, 'Publicações', 'publicação', 'edu:publica_create', rows, ['ID', 'Autor', 'Livro', 'ISBN'])


def publica_create(request):
    form = PublicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('edu:publica_list')
    return render(request, 'edu/form.html', {'title': 'Nova publicação', 'form': form})


def publica_update(request, pk):
    publica = get_object_or_404(Publica, pk=pk)
    form = PublicaForm(request.POST or None, instance=publica)
    if form.is_valid():
        form.save()
        return redirect('edu:publica_list')
    return render(request, 'edu/form.html', {'title': 'Editar publicação', 'form': form})


def publica_delete(request, pk):
    publica = get_object_or_404(Publica, pk=pk)
    if request.method == 'POST':
        publica.delete()
        return redirect('edu:publica_list')
    return render(request, 'edu/delete.html', {'title': 'Excluir publicação', 'object': publica, 'cancel_url': 'edu:publica_list'})
