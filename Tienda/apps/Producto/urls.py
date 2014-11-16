from django.conf.urls import patterns, include, url
from .views import *
urlpatterns = patterns('',
    url(r'^$',inicio_view , name='Inicio'),
    url(r'^Producto/registro/$',registro_view),
    url(r'^Producto/pedidos/$',pedidos_view),

)