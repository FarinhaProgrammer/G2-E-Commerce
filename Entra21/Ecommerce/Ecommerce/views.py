from django.shortcuts import render
from categorias.models import Categoria, Tag
from categorias.views import categoria_queryset_parser
from produtos.forms import SearchForm
from produtos.models import Produto
from produtos.views import produto_queryset_parser

def home(request):
    if request.method == 'POST':
        return search(request)
    else:
        form = SearchForm()
    categorias = Categoria.objects.all()
    categorias = categoria_queryset_parser(categorias)
    return render(request, 'home.html', {'categorias': categorias, 'form': form})

def search(request):
    form = SearchForm(request.POST)
    products_tags_products_parsed = []
    if form.is_valid():
        result = form.cleaned_data['result']
        result_broke = result.split()
        products = Produto.objects.all().filter(nome__icontains=result)
        products = produto_queryset_parser(products)
        products_tags = Tag.objects.all().filter(nome__in=result_broke)
        products_tags_products = [t.produtos.all() for t in products_tags]
        for qs in products_tags_products:
            qs_parsed = produto_queryset_parser(qs)
            for p in qs_parsed:
                products_tags_products_parsed.append(p)
        products_tags_products = [p for p in products_tags_products_parsed if p not in products]
        products = products + products_tags_products_parsed
    
    return render(request, 'produtos/produtos.html', {'dados':products, 'titulo':'Resultados'})
