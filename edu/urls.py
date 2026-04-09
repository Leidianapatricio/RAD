from django.urls import path
from . import views

app_name = 'edu'

urlpatterns = [
    path('', views.index, name='index'),
    path('livros/', views.livro_list, name='livro_list'),
    path('autores/', views.autor_list, name='autor_list'),
    path('autores/novo/', views.autor_create, name='autor_create'),
    path('autores/<int:pk>/editar/', views.autor_update, name='autor_update'),
    path('autores/<int:pk>/excluir/', views.autor_delete, name='autor_delete'),

    path('editoras/', views.editora_list, name='editora_list'),
    path('editoras/novo/', views.editora_create, name='editora_create'),
    path('editoras/<int:pk>/editar/', views.editora_update, name='editora_update'),
    path('editoras/<int:pk>/excluir/', views.editora_delete, name='editora_delete'),
    path('livros/', views.livro_list, name='livro_list'),
    path('livros/novo/', views.livro_create, name='livro_create'),
    path('livros/<int:pk>/editar/', views.livro_update, name='livro_update'),
    path('livros/<int:pk>/excluir/', views.livro_delete, name='livro_delete'),

    path('publicacoes/', views.publica_list, name='publica_list'),
    path('publicacoes/novo/', views.publica_create, name='publica_create'),
    path('publicacoes/<int:pk>/editar/', views.publica_update, name='publica_update'),
    path('publicacoes/<int:pk>/excluir/', views.publica_delete, name='publica_delete'),
]