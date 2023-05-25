from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    estoque = models.PositiveIntegerField()

class Carrinho(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)

class CustomUser(AbstractUser):
    receber_emails = models.BooleanField(default=False)
    time_coracao = models.CharField(max_length=255, null=True, blank=True)

class Avaliacao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avaliacao = models.IntegerField()
    comentario = models.TextField()

    class Meta:
        verbose_name_plural = 'Avaliacoes'

class Compra(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

class Cartao(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=16)
    expiracao_mes = models.PositiveIntegerField()
    expiracao_ano = models.PositiveIntegerField()
    cvv = models.CharField(max_length=3)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    tracking_number = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default='Pedido Recebido')

    def __str__(self):
        return f'Pedido {self.id} - {self.product}'
    
class Devolucao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    numero_pedido = models.CharField(max_length=200)
    produto = models.CharField(max_length=200)
    comentario = models.TextField()
    data_devolucao = models.DateTimeField(auto_now_add=True)
