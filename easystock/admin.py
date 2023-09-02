from django.contrib import admin
from easystock.models import Produto, Tipo, Classificacoe

class Produtos (admin.ModelAdmin):
    list_display = ('id','nome', 'valor')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Produto, Produtos)

class Tipos (admin.ModelAdmin):
    list_display = ('id', 'departamentos', 'descricao')
    list_display_links = ('id', 'departamentos')
    search_fields = ('departamentos',)
    list_per_page = 20

admin.site.register(Tipo, Tipos)

class Classificacao1 (admin.ModelAdmin):
    list_display = ('id', 'produto', 'tipo')
    list_display_links = ('id',)

admin.site.register(Classificacoe, Classificacao1)
