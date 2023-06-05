from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import TeamSelectionForm
from .models import Carrinho, ItemCarrinho, Produto
from .forms import AvaliacaoForm
from .models import Compra, Cartao
from .forms import CompraForm, CartaoForm
import stripe
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Order
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')

    elif request.method == "POST":
        try:
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            receber_emails = True

            user = CustomUser.objects.create_user(email=email, username=username, password=password, receber_emails=receber_emails)

            user.save()
            request.session['user_id'] = user.id  
            return redirect('team_selection')
        except Exception as error:
            print(error)
            return HttpResponse('Erro: {}'.format(error))

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Nome de usuário ou senha inválidos.')

    return render(request, 'login.html')

def home(request):
    if request.method == "GET":
        query = request.GET.get('q')
        produtos = Produto.objects.all()

        if query:
            produtos = produtos.filter(nome__icontains=query)

        return render(request, 'home.html', {'produtos': produtos})

    elif request.method == "POST" and request.user.is_authenticated:
        produto_id = request.POST.get('produto_id')
        produto = get_object_or_404(Produto, id=produto_id)

        carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)

        # Verifica se o item já está presente no carrinho
        item_carrinho, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)

        if not created:
            # Se o item já existe, incrementa a quantidade
            item_carrinho.quantidade += 1
        else:
            # Se o item é criado, inicializa o valor total_item
            item_carrinho.preco = produto.preco
            item_carrinho.quantidade = 1

        item_carrinho.save()

        return redirect('carrinho')

    else:
        return redirect('login')

def team_selection(request):
    if request.method == 'POST':
        form = TeamSelectionForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']

            user_id = request.session.get('user_id')  # Obtenha o ID do usuário da sessão
            if user_id:
                user = CustomUser.objects.get(pk=user_id)
                user.time_coracao = team
                user.save()
                del request.session['user_id']  # Remova o ID do usuário da sessão

            return render(request, 'confirmation.html', {'team': team})
    else:
        form = TeamSelectionForm()

    return render(request, 'team_selection.html', {'form': form})


def inicial(request):
    return render(request, 'inicial.html')

def carrinho(request):
    if request.user.is_authenticated:
        carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
        itens_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho)

        total = 0

        for item_carrinho in itens_carrinho:
            item_carrinho.total_item = item_carrinho.preco * item_carrinho.quantidade
            item_carrinho.save()
            total += item_carrinho.total_item

        carrinho.total_compra = total
        carrinho.save()

        return render(request, 'carrinho.html', {'itens_carrinho': itens_carrinho, 'total': total})
    else:
        return redirect('login')

def remover_item_carrinho(request, item_carrinho_id):
    item_carrinho = get_object_or_404(ItemCarrinho, id=item_carrinho_id)
    item_carrinho.quantidade -= 1
    
    if item_carrinho.quantidade <= 0:
        item_carrinho.delete()
    else:
        item_carrinho.save()
    
    return redirect('carrinho')

def avaliar(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = request.user
            avaliacao.save()
            return redirect('home')
    else:
        form = AvaliacaoForm()
    return render(request, 'avaliar.html', {'form': form})

stripe.api_key = settings.STRIPE_SECRET_KEY

def confirmar_compra(request):
    if request.method == 'POST':
        form_compra = CompraForm(request.POST)
        form_cartao = CartaoForm(request.POST)

        if form_compra.is_valid() and form_cartao.is_valid():
            compra = form_compra.save(commit=False)
            compra.user = request.user
            compra.save()

            cartao = form_cartao.save(commit=False)
            cartao.user = request.user
            cartao.save()

            # Efetue a cobrança no Stripe
            stripe.Charge.create(
                amount=int(compra.valor * 100),
                currency='brl',
                description=compra.descricao,
                source=request.POST['stripeToken'],
            )

            # Redirecionar para 'rastrear' após a confirmação da compra
            return redirect('rastrear')

    else:
        form_compra = CompraForm()
        form_cartao = CartaoForm()

    return render(request, 'rastrear.html', {'form_compra': form_compra, 'form_cartao': form_cartao, 'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})


def adicionar_cartao(request):
    if request.method == 'GET':
        form = CartaoForm()
        return render(request, 'pagamento/adca_cartao.html', {'form': form})
    else:
        form = CartaoForm(request.POST)
        if form.is_valid():
            cartao = form.save(commit=False)
            cartao.user = request.user
            cartao.save()

            return redirect(reverse('pagamento:confirmar_compra'))
        else:
            return render(request, 'pagamento/adca_cartao.html', {'form': form})
        
def finalizar_compra(request):
    
    return render(request, 'adca_cartao.html')

def buscar_produto(request):
    query = request.GET.get('q')
    if query:
        produtos = Produto.objects.filter(nome__icontains=query)
    else:
        produtos = Produto.objects.all()
    return render(request, 'home.html', {'produtos': produtos})

def get_status_from_tracking_api(tracking_number):
    # Aqui você iria fazer a chamada à API de rastreamento.
    # Para manter as coisas simples, retornaremos um status fixo.
    return "Em trânsito"

def update_order_status(order):
    status = get_status_from_tracking_api(order.tracking_number)
    order.status = status
    order.save()

@login_required
def order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.user != request.user:
        raise PermissionDenied
    update_order_status(order)
    return render(request, 'order_status.html', {'order': order})

def rastrear(request):
    return render(request, 'pagamento/rastrear.html')

def devolucao_produto(request):
    if request.method == 'POST':
        # Processar o formulário aqui
        produto_id = request.POST.get('produto_id')
        motivo = request.POST.get('motivo')
        # Faça o que precisar com os dados do formulário

        # Redirecionar para uma página de confirmação ou outra página desejada
        return redirect('pagina_de_confirmacao')

    else:
        # Renderizar o formulário
        return render(request, 'devolucao.html')
