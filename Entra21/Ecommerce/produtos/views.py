from produtos.models import Produto
from django.shortcuts import render, get_object_or_404
from categorias.models import Categoria
from .models import Produto
from random import randint

def bubblesort(v, n, key):
    """
    Esta função é um método de ordenação muito conhecido, onde as informações são comparadas em pares,
    e vão sendo realocadas dependendo do resultado da comparação.
    """
    if n < 1:
        return
    
    for i in range(n):
        if v[i][key] < v[i + 1][key]:
            temp = v[i]
            v[i] = v[i + 1]
            v[i + 1] = temp

    bubblesort(v, n - 1)


def retorna_produtos(request):
    """
    Retorna os objetos do modelo Produto.
    """
    dados = Produto.objects.all()
    return render(request, 'produtos/produtos.html', {'dados':dados})


def retorna_produtos_mais_vendidos(request):
    """
    Esta função retorna um vetor com os 20 produtos mais vendidos, na ordem decrescente,
    utilizando do método de ordenação, bubblesort, o qual compara os itens em pares,
    e realiza trocas entre os mesmos.
    """
    dados = Produto.objects.all()
    mais_vendidos = list(dados)
    bubblesort(mais_vendidos, len(mais_vendidos) - 1, 'vendas')
    return render(request, 'produtos/produtos.html', {'dados': mais_vendidos[:20], 'titulo':'Mais Vendidos'})


def retorna_produtos_mais_visualizados(request):
    """
    Esta função retorna um vetor com os 20 produtos mais vistos, na ordem decrescente,
    utilizando do método de ordenação, bubblesort, o qual compara os itens em pares,
    e realiza trocas entre os mesmos.
    """
    dados = Produto.objects.all()
    mais_visualizados = list(dados)
    bubblesort(mais_visualizados, len(mais_visualizados) - 1, 'visualizacoes')
    mais_visualizados = mais_visualizados[:20]
    for i in mais_visualizados:
        i['categoria'] = get_object_or_404(Categoria, id=i['categoria']).nome
    return render(request, 'produtos/produtos.html', {'dados':mais_visualizados, 'titulo':'Mais Visitados'})


def retorna_produtos_mais_recentes(request):
    """
    Esta função retorna um vetor com os 20 produtos mais recentes cadastrados no banco de dados,
    utilizando os métodos mágicos na classe Produto para fazer a comparação entre as datas,
    essas comparações sendo feitas utilizando a biblioteca datetime.
    """
    dados = Produto.objects.all()
    dados = list(dados)
    dados = dados.sort(reverse=True)
    dados = dados[:20]
    return render(request, 'produtos/produtos.html', {'dados':dados, 'titulo':'Lançamentos'})


def detalhes_produto(request, pk):
    """
    Esta função retorna os dados do produto selecionado.
    """
    produto = get_object_or_404(Produto, pk=pk)
    dados = Produto.objects.all()
    dados = list(dados)
    recomendacao = []
    for _ in range(3):
        reco = dados[randint(0, len(dados) - 1)]
        if reco not in recomendacao:
            recomendacao.append
    return render(request, 'produtos/detalhes_produto.html', {'i': produto, 'dados': recomendacao, 'nome': 'Produto'})