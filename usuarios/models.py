from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    estoque = models.PositiveIntegerField()

class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)

class UsuariosCarrinhoMixin:
    def adicionar_produto(self, produto, quantidade=1):
        item_carrinho, criado = ItemCarrinho.objects.get_or_create(
            produto=produto,
            carrinho=self
        )
        if not criado:
            item_carrinho.quantidade += quantidade
            item_carrinho.save()
