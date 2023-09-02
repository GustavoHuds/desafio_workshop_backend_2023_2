from django.shortcuts import render
from rest_framework import viewsets, generics
from easystock.models import Produto, Tipo, Classificacoe
from .serializers import ProdutoSerializer, TipoSerializer, ClassificacoeSerializer, FiltrarTiposSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ProdutosViewSet(viewsets.ModelViewSet):
    """Exibindo os produtos"""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class TiposViewSet(viewsets.ModelViewSet):
    """Exibindo os tipos de produto"""
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class Classificacoe1ViewSet(viewsets.ModelViewSet):
    """Listando as classificações dos produtos"""
    queryset = Classificacoe.objects.all()
    serializer_class = ClassificacoeSerializer

class FiltrarTipos(generics.ListAPIView):
    """Filtrando os produtos por tipo"""
    """Recuperando a informação do tipo pelo id"""
    def get_queryset(self):
        queryset = Classificacoe.objects.filter(tipo_id=self.kwargs['pk'])
        return queryset
    serializer_class = FiltrarTiposSerializer
