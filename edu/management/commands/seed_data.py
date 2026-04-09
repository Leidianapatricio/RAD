from django.core.management.base import BaseCommand
from edu.models import Autor, Editora, Livro, Publica
from django.db import transaction


class Command(BaseCommand):
    help = 'Populate sample data for edu app (autor/editora/livro/publica)'

    def handle(self, *args, **options):
        with transaction.atomic():
            editora, _ = Editora.objects.get_or_create(nome='Companhia das Letras')
            autor1, _ = Autor.objects.get_or_create(nome='Machado de Assis')
            autor2, _ = Autor.objects.get_or_create(nome='Clarice Lispector')

            livro1, _ = Livro.objects.get_or_create(
                isbn='9788535902816',
                defaults={
                    'titulo': 'Dom Casmurro',
                    'publicacao': '1899-01-01',
                    'preco': '39.90',
                    'estoque': 5,
                    'editora': editora,
                }
            )
            livro2, _ = Livro.objects.get_or_create(
                isbn='9788539001234',
                defaults={
                    'titulo': 'A Hora da Estrela',
                    'publicacao': '1977-01-01',
                    'preco': '29.90',
                    'estoque': 8,
                    'editora': editora,
                }
            )

            Publica.objects.get_or_create(livro=livro1, autor=autor1)
            Publica.objects.get_or_create(livro=livro2, autor=autor2)

            self.stdout.write(self.style.SUCCESS('Seed concluído: Autor/Editora/Livro/Publica criados ou encontrados.'))
