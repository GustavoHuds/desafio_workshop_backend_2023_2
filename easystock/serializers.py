from rest_framework import serializers
from .models import Produto, Tipo, Classificacoe

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        exclude = []

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        exclude = []

class ClassificacoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classificacoe
        exclude = []

class FiltrarTiposSerializer(serializers.ModelSerializer):
    produto_nome = serializers.ReadOnlyField(source='produto.nome')
    class Meta:
        model = Classificacoe
        fields = ['produto']