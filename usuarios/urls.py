from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView


app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('perfil/<int:pk>/', views.Perfil.as_view(), name='perfil'),
    path('perfil/editar/', views.EditarPerfil, name='editar_perfil'),
    path('perfil/editar/password', views.EditarPassword.as_view(), name='password'),
]
