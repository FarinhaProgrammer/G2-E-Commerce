from django.shortcuts import render
from categorias.models import Categoria
from Ecommerce.forms import SearchForm
from produtos.views import search

def home(request):
    if request.method == 'POST':
        return search(request)
    else:
        form = SearchForm()
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {'categorias': categorias, 'form': form})
