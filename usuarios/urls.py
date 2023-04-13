from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name = "cadastro"),
    path('login/', views.login, name = "login"),
    path('home/', views.home, name="home"),
    path('adicionar_ao_carrinho/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('confirmar_compra/', views.confirmar_compra, name = "confirmar_compra"),
    path('team_selection/', views.team_selection, name="team_selection"),


]

