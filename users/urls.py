from django.urls import path
from . import views

urlpatterns = [
    path('registro/',views.registro_usuario, name='registro'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
]