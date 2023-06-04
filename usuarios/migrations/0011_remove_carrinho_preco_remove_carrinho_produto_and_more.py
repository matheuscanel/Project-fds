# Generated by Django 4.2.1 on 2023-06-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_alter_carrinho_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='preco',
        ),
        migrations.RemoveField(
            model_name='carrinho',
            name='produto',
        ),
        migrations.AddField(
            model_name='carrinho',
            name='produtos',
            field=models.ManyToManyField(through='usuarios.ItemCarrinho', to='usuarios.produto'),
        ),
        migrations.AddField(
            model_name='itemcarrinho',
            name='quantidade',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
