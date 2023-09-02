from django.contrib import admin
from django.urls import path, include
from easystock.views import ProdutosViewSet, TiposViewSet, Classificacoe1ViewSet, FiltrarTipos
from easystock.models import Produto, Tipo, Classificacoe
from rest_framework import routers

router = routers.DefaultRouter()
router.register('produto', ProdutosViewSet, basename='Produtos')
router.register('tipo', TiposViewSet, basename='Tipos')
router.register('classificacoe', Classificacoe1ViewSet, basename='Classificacoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('tipo/<int:pk>classificacoe/',FiltrarTipos.as_view())
]
