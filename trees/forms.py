from django import forms
from . import models

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
        label='Usuário',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        label='Senha',
    )

class AddPlantedTreeForm(forms.ModelForm):
    class Meta:
        model = models.PlantedTree
        fields = ['account', 'tree', 'latitude', 'longitude']

        widgets = {
            'account': forms.Select(attrs={'class':'form-select bg-dark text-white'}),
            'tree': forms.Select(attrs={'class':'form-select bg-dark text-white'}),
            'latitude': forms.TextInput(attrs={'class':'form-control bg-dark text-white'}),
            'longitude': forms.TextInput(attrs={'class':'form-control bg-dark text-white'}),
        }

        labels = {
            'account': 'Conta',
            'tree': 'Árvore',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
        }