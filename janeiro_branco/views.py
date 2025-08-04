# janeiro_branco/views.py
from django.shortcuts import render, redirect
from .forms import MensagemDeApoioForm
from .models import MensagemDeApoio

def home(request):
    # Lida com o envio do formulário
    if request.method == 'POST':
        form = MensagemDeApoioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona para evitar reenvio do formulário
    else:
        form = MensagemDeApoioForm()

    # Busca todas as mensagens do banco de dados, ordenando pelas mais recentes
    mensagens = MensagemDeApoio.objects.all().order_by('-data_envio')

    contexto = {
        'form': form,
        'mensagens': mensagens
    }
    return render(request, 'janeiro_branco/index.html', contexto)