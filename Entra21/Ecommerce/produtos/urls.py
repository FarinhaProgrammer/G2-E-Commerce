from produtos.views import retorna_produtos, retorna_produtos_mais_recentes, retorna_produtos_mais_vendidos, retorna_produtos_mais_visualizados, detalhes_produto
from django.urls import path

app_name = 'produtos'

"""
URLs do app produtos.
"""

urlpatterns = [
    path('<int:pk>/', detalhes_produto, name='retrieve'),
    path('list/', retorna_produtos, 'list'),
    path('maisVendidos/', retorna_produtos_mais_vendidos, name='maisVendidos'),
    path('maisVistos', retorna_produtos_mais_visualizados, name='maisVistos'),
    path('lancamentos/', retorna_produtos_mais_recentes, name='lancamentos'),
]