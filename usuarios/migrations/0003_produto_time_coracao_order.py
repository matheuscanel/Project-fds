# Generated by Django 4.1.7 on 2023-05-25 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_avaliacao_cartao_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='time_coracao',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('tracking_number', models.CharField(max_length=200)),
                ('status', models.CharField(default='Pedido Recebido', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
