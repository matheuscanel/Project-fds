from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from .forms import TeamSelectionForm, CadastroForm
from django.shortcuts import redirect
from .models import Carrinho, ItemCarrinho, Produto
from .forms import AvaliacaoForm
from .models import Compra, Cartao
from .forms import CompraForm, CartaoForm
import stripe
from django.conf import settings

def cadastro(request):
    if request.method == "GET":
        form = CadastroForm()
        return render(request, 'cadastro.html', {'form': form})

    else:
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            request.session['user_id'] = user.id  

            return redirect('team_selection')
        else:
            return render(request, 'cadastro.html', {'form': form})


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


def home(request):
    if request.method == "GET":
        return render(request, 'home.html')


def confirmar_compra(request):
    if request.method == "GET":
        return HttpResponse("Tela de confirmar compra")  # retornar o html
    else:
        return


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


def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)

    item, criado = ItemCarrinho.objects.get_or_create(
        produto=produto,
        carrinho=carrinho
    )

    if not criado:
        item.quantidade += 1
        item.save()

    return redirect('nome_da_view_da_loja')


def inicial(request):
    return render(request, 'inicial.html')


def exibir_carrinho(request):
    try:
        carrinho = Carrinho.objects.get(usuario=request.user)
        itens_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho)
    except Carrinho.DoesNotExist:
        carrinho = None
        itens_carrinho = None

    context = {
        'carrinho': carrinho,
        'itens_carrinho': itens_carrinho,
    }

    return render(request, 'carrinho.html', context)

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

            return render(request, 'pagamento/sucesso.html')
    else:
        form_compra = CompraForm()
        form_cartao = CartaoForm()

    return render(request, 'pagamento/confirmar_compra.html', {'form_compra': form_compra, 'form_cartao': form_cartao, 'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})