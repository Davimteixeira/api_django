from django.contrib import admin
from django.urls import path, include
from clientes.views import ClientesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'clientes', ClientesViewSet, basename='Cliente') 


urlpatterns = [
    path('', include(router.urls)),
]