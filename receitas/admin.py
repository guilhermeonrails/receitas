from django.contrib import admin
from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'pessoa', 'tempo_preparo', 'rendimento', 'data_receita', 'publicada')
    list_display_links = ('id', 'nome_receita')
    list_filter = ('pessoa','tempo_preparo',)
    list_editable = ('publicada',)
    search_fields = ('nome_receita',)
    list_per_page = 1

admin.site.register(Receita, ListandoReceitas)