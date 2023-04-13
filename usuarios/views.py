from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django. contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .forms import TeamSelectionForm
from django.shortcuts import redirect

def cadastro(request):
        if request.method == "GET":
        
            return render(request, 'cadastro.html')
        
        else: 
            username = request.POST.get('username')
            email= request.POST.get('email')
            senha = request.POST.get('senha')

            user = User.objects.filter(username = username).first()

            if user:
                  return HttpResponse('Ja existe um usuario com esse nome')
            
            user = User.objects.create_user(username = username, email = email, password = senha)
            user.save()

            return redirect ('team_selection') #teste

def login(request):
        if request.method == "GET":
            return render(request, 'login.html')
        
        else:
            username = request.POST.get('username')
            senha = request.POST.get('senha')

            user = authenticate(username=username, password=senha)

            if user:
                login_django(request, user)
                return redirect('home')
            else:
                return HttpResponse('Email ou senha invalidos')
            

@login_required(login_url= "/usuarios/login")

def home(request):
        if request.method == "GET":
        
            return render(request, 'home.html')
        
def confirmar_compra (request):
    if request.method == "GET":
        return HttpResponse("Tela de confirmar compra") #retornar o html
    else: 

        return

def team_selection(request):
    if request.method == 'POST':
        form = TeamSelectionForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            # Aqui você pode adicionar o que você quer fazer com a seleção do time
            return render(request, 'confirmation.html', {'team': team})
    else:
        form = TeamSelectionForm()

    return render(request, 'team_selection.html', {'form': form})
        

from .models import Carrinho, ItemCarrinho, Produto

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404 (Produto, pk=produto_id)
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
    
    item, criado = ItemCarrinho.objects.get_or_create(
        produto=produto,
        carrinho=carrinho
    )

    if not criado:
        item.quantidade += 1
        item.save()

    return redirect('nome_da_view_da_loja')

    
