# janeiro_branco/forms.py
from django import forms
from .models import MensagemDeApoio

class MensagemDeApoioForm(forms.ModelForm):
    class Meta:
        model = MensagemDeApoio
        fields = ['nome', 'email', 'telefone', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu Nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Seu Email (válido)'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Seu Telefone'}),
            'mensagem': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Digite sua mensagem aqui...'})
        }
        labels = {
            'nome': '',
            'email': '',
            'telefone': '',
            'mensagem': ''
        }