from django.urls import path
from inicio import views
from inicio.views import (
    inicio, 
    buscar_ropa, 
    about, 
    editar_ropa)

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('home/', views.home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('nueva-ropa/', views.CargarRopa.as_view(), name='nueva_ropa'),
    path('buscar-ropa/', buscar_ropa, name='buscar_ropa'),
    path('ver-ropa/<int:pk>/', views.ver_ropa.as_view(), name='ver_ropa'),
    path('eliminar-ropa/<int:pk>/', views.eliminar_ropa.as_view(), name='eliminar_ropa'),
    path('editar-ropa/<int:pk>/', views.editar_ropa.as_view(), name='editar_ropa'),
    
    ]
