from django.db import models
from django.contrib.auth.models import User
from .models import Produto

class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)

