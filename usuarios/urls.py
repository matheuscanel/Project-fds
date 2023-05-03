from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login, name="login"),
    path('home/', views.home, name="home"),  
    path('confirmar_compra/', views.confirmar_compra, name="confirmar_compra"),
    path('team_selection/', views.team_selection, name="team_selection"),
    path('', views.inicial, name="inicial"),
    path('usuarios/carrinho/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/', views.exibir_carrinho, name='exibir_carrinho'),
    path('avaliar/', views.avaliar, name='avaliar'),

]
