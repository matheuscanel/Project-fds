# Generated by Django 4.1.7 on 2023-05-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_remove_produto_time_alter_customuser_time_coracao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='equipe',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
