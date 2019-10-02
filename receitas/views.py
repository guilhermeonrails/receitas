from django.shortcuts import render
from .models import Receita
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    paginator = Paginator(receitas, 2)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    dados = {
        'receitas': receitas_por_pagina
    }
    return render(request, 'index.html', dados)

def contato(request):
    return render(request, 'contato.html')

def receita(request, receita_id):
    return render(request, 'receita.html')