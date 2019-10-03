from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from receitas.categorias import tipos_de_receitas

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
    receita = get_object_or_404(Receita,pk=receita_id)

    receita_a_exibir = {
        'receita' : receita,
        'tipos_de_receitas' : tipos_de_receitas
    }

    return render(request, 'receita.html', receita_a_exibir)