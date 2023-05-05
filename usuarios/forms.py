from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Avaliacao
from .models import Compra, Cartao


class TeamSelectionForm(forms.Form):
   OPTIONS = [
       ('Sport', 'Sport'),
       ('Náutico', 'Náutico'),
       ('Santa Cruz', 'Santa Cruz'),
       ('Bahia', 'Bahia'),
       ('Vitória', 'Vitória'),
       ('Ceará', 'Ceará'),
       ('Fortaleza', 'Fortaleza'),
       ('CSA', 'CSA'),
       ('CRB', 'CRB'),
       ('ABC', 'ABC'),
       ('América', 'América'),
       ('Sampaio Correia', 'Sampaio Correia'),
       ('Campinese', 'Campinese'),
       ('Botafogo', 'Botafogo'),
       ('River-pi', 'River-pi'),
       ('Salgueiro', 'Salgueiro'),
   ]


   team = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect)


class CadastroForm(UserCreationForm):
   class Meta:
       model = CustomUser
       fields = ['username', 'email', 'password1', 'password2', 'receber_emails']
       widgets = {
           'receber_emails': forms.CheckboxInput(attrs={'class': 'form-check-input'})
       }


class AvaliacaoForm(forms.ModelForm):
   class Meta:
       model = Avaliacao
       fields = ['avaliacao', 'comentario']
       widgets = {
           'avaliacao': forms.RadioSelect,
       }




class CompraForm(forms.ModelForm):
   class Meta:
       model = Compra
       fields = ['descricao', 'valor']


class CartaoForm(forms.ModelForm):
   class Meta:
       model = Cartao
       fields = ['nome', 'numero', 'expiracao_mes', 'expiracao_ano', 'cvv']


