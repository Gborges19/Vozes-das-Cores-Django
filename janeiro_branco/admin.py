# janeiro_branco/admin.py
from django.contrib import admin
from .models import MensagemDeApoio

# Registra seu modelo para que ele apareça no painel de admin
admin.site.register(MensagemDeApoio)