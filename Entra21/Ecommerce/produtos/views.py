from produtos.models import Produto
from django.shortcuts import get_list_or_404, render, get_object_or_404
import requests
from categorias.models import Categoria
from .models import Produto
from random import randint

def bubblesort(v, n):

    if n < 1:
        return
    
    for i in range(n):
        if v[i]['vendas'] < v[i + 1]['vendas']:
            temp = v[i]
            v[i] = v[i + 1]
            v[i + 1] = temp

    bubblesort(v, n - 1)


def retorna_produtos(request):
    """
    Esta função retorna os dados da api, obtidos através do consumo da mesma pela url.

    O retorno consiste em um template acompanhado de um json.
    """
    dados = Produto.objects.all()
    return render(request, 'produtos/produtos.html', {'dados':dados})


def retorna_produtos_mais_vendidos(request):
    """
    Esta função retorna um vetor com os 20 produtos mais vendidos, na ordem decrescente,
    utilizando do método de ordenação, bubblesort, o qual compara os itens em pares,
    e realiza trocas entre os mesmos.
    """
    dados = requests.get('http://127.0.0.1:8000/api/produtos')
    dados = dados.json()
    maior = list(dados)
    bubblesort(maior, len(maior) - 1)
    return render(request, 'produtos/produtos.html', {'dados': maior[:20], 'titulo':'Mais Vendidos'})


def retorna_produtos_mais_visualizados(request):
    """
    Esta função retorna um vetor com os 20 produtos mais vistos, na ordem decrescente,
    utilizando os métodos mágicos para fazer comparações entre os produtos e determinar qual tem mais visitas.
    """
    dados = requests.get('http://127.0.0.1:8000/api/produtos')
    dados = dados.json()
    maior = list(dados)
    bubblesort(maior, len(maior) - 1)
    maior = maior[:20]
    for i in maior:
        i['categoria'] = get_object_or_404(Categoria, id=i['categoria']).nome
    return render(request, 'produtos/produtos.html', {'dados':maior, 'titulo':'Mais Visitados'})


def detalhes_produto(request, pk):
    """
    Esta função retorna os dados do produto selecionado.
    """
    produto = requests.get('http://127.0.0.1:8000/api/produtos/' + str(pk) + '/')
    produto = produto.json()
    dados = requests.get('http://127.0.0.1:8000/api/produtos/')
    dados = dados.json()
    dados = list(dados)
    recomendacao = [dados[randint(0, (len(dados)-1))] for i in range((len(dados)-1))]
    while(recomendacao[0]==recomendacao[1] or recomendacao[1]==recomendacao[2] or recomendacao[2]==recomendacao[0]):
        recomendacao = [dados[randint(0, (len(dados)-1))] for i in range((len(dados)-1))]
    return render(request, 'produtos/detalhes_produto.html', {'i': produto, 'dados': recomendacao[:3], 'nome': 'Produto'})

def retorna_produtos_categoria(request, pk):
    """
    Esta função retorna os produtos de determinada categoria.
    """
    categoria = requests.get('http://127.0.0.1:8000/api/categorias/' + str(pk) + '/')
    categoria = categoria.json()
    produtos = get_list_or_404(Produto, categoria=categoria.id)
    return render(request, 'produtos/produtos.html', {'dados': produtos, 'titulo':categoria.nome})
