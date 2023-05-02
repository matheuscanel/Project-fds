from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

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
