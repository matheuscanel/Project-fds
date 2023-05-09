from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    estoque = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Carrinho de {self.usuario.username}'


class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome} ({self.carrinho.usuario.username})'


class UsuariosCarrinhoMixin:
    def adicionar_produto(self, produto, quantidade=1):
        item_carrinho, criado = ItemCarrinho.objects.get_or_create(
            produto=produto,
            carrinho=self
        )
        if not criado:
            item_carrinho.quantidade += quantidade
            item_carrinho.save()


class CustomUser(AbstractUser):
    receber_emails = models.BooleanField(default=False)
    time_coracao = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username


class Avaliacao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    avaliacao = models.IntegerField()
    comentario = models.TextField()

    class Meta:
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return f'Avaliação de {self.avaliacao} estrelas no produto {self.produto.nome}'


class Compra(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Compra de {self.usuario.username} no valor de {self.valor}'


class Cartao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=16)
    expiracao_mes = models.PositiveIntegerField()
    expiracao_ano = models.PositiveIntegerField()
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return f'Cartão de {self.usuario.username} - {self.numero[-4:]}'
