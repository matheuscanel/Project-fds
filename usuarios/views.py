from django.shortcuts import render
from django.http import HttpResponse
from django. contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

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

            return render(request, 'login.html') #teste

def login(request):
        if request.method == "GET":
            return render(request, 'login.html')
        
        else:
            username = request.POST.get('username')
            senha = request.POST.get('senha')

            user = authenticate(username=username, password=senha)

            if user:
                login_django(request, user)
                return render(request, 'home.html')
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
        

    
