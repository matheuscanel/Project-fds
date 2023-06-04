from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('carrinho/remover/<int:item_carrinho_id>/', views.remover_item_carrinho, name='remover_item'),
    path('login/', views.login_view, name="login"),
    path('home/', views.home, name="home"),
    path('team_selection/', views.team_selection, name="team_selection"),
    path('', views.inicial, name="inicial"),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('avaliar/', views.avaliar, name='avaliar'),
    path('confirmar_compra/', views.confirmar_compra, name='confirmar_compra'),
    path('carrinho/finalizar/', views.finalizar_compra, name='finalizar_compra'),
    path('buscar/', views.buscar_produto, name='buscar_produto'),
    path('order_status/<int:order_id>/', views.order_status, name='order_status'),
    path('rastrear/', views.rastrear, name='rastrear'),
    path('devolucao.html', views.devolucao_produto, name='devolucao_produto'),
]
