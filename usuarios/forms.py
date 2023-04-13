from django import forms

class TeamSelectionForm(forms.Form):
    OPTIONS = [
        ('Sport', 'Sport'),
        ('Náutico', 'Náutico'),
        ('Santa', 'Santa'),
        ('Bahia', 'Bahia'),
        ('Vitoria', 'Vitoria'),
        ('Ceara', 'Ceara'),
        ('Fortaleza', 'Fortaleza'),
        ('CSA', 'CSA'),
        ('CRB', 'CRB'),
        ('ABC', 'ABC'),
        ('America', 'America'),
        ('Sampaio', 'Sampaio'),
        ('Campinese', 'Campinese'),
        ('Botafogo', 'Botafogo'),
        ('River', 'River'),
        ('Salgueiro', 'Salgueiro'),
    ]

    team = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect)