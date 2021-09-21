from produtos.views import recomendacao
from django.shortcuts import render, get_object_or_404
from produtos.models import Produto
from carrinho.models import Carrinho

def retorna_carrinho(request, pk=None):
    """
    O retorno consiste em um template acompanhado de um json com os dados do carrinho.
    """
    if request.user.is_authenticated:
        try:
            dados = get_object_or_404(Carrinho, pk=pk)
        except:
            no_match = True
            if pk != request.user.id:
                return render(request, 'carrinho/erro-carrinho.html')
        else:
            if pk != request.user.carrinho.id:
                return render(request, 'carrinho/erro-carrinho.html')

            produtos = [get_object_or_404(Produto, id=i.id) for i in dados.produtos.all()]

            # total do carrinho
            total_itens = len(produtos)
            total = [i.preco for i in produtos]
            total = sum(total)
            
            return render(request, 'carrinho/carrinho.html', {'dados': produtos, 'total_itens': total_itens, 'total': total, 'no_match': False})

        return render(request, 'carrinho/carrinho.html', {'no_match': no_match})
    else:
        try:
            products = request.session['cart_products'][:]
        except:
            request.session['cart_products'] = []
            return render(request, 'carrinho/carrinho.html', {'no_match': True})
        else:
            if len(products) == 0:
                return render(request, 'carrinho/carrinho.html', {'no_match': True})
            else:
                total_itens = len(products)
                total = [i.preco for i in products]
                total = sum(total)
                
                return render(request, 'carrinho/carrinho.html', {'dados': products, 'total_itens': total_itens, 'total': total, 'no_match': False})


def adicionar(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.user.is_authenticated:
        carrinho = get_object_or_404(Carrinho, id=request.user.carrinho.id)
        carrinho.produtos.add(produto)
    else:
        try:
            products = request.session['cart_products'][:]
        except:
            request.session['cart_products'] = []

        request.session['cart_products'].append(produto)

    reco = recomendacao(Produto.objects.all(), produto)
    return render(request, 'produtos/detalhes_produto.html', {'produto':produto, 'dados':reco, 'nome':'Produto', 'success': True, 'in_cart': True})


def remover(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.user.is_authenticated:
        carrinho = get_object_or_404(Carrinho, id=request.user.carrinho.id)
        carrinho.produtos.remove(produto)
    else:
        try:
            products = request.session['cart_products'][:]
        except:
            request.session['cart_products'] = []
            products = request.session['cart_products'][:]

        products.pop(produto)

    reco = recomendacao(Produto.objects.all(), produto)
    return render(request, 'produtos/detalhes_produto.html', {'produto':produto, 'dados':reco, 'nome':'Produto', 'success': False, 'in_cart': False})
