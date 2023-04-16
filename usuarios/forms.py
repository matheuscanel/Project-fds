from django import forms

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