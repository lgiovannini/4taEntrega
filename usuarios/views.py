from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login
from django.urls import reverse_lazy
from usuarios.forms import FormRegistro, FormEdicion
from usuarios.models import ExtraData
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':    
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():

            usuario = formulario.get_user()
            django_login(request, usuario)
            
            ExtraData.objects.get_or_create(user=usuario)
            
            return redirect('inicio:home')
    return render(request, 'usuarios/login.html', {'form': formulario})

def register(request):
    
    formulario = FormRegistro()
    if request.method == 'POST':
        
        formulario = FormRegistro(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            return redirect('usuarios:login')
    
    return render(request, 'usuarios/register.html', {'form': formulario})

class Perfil(DetailView):
    model = User
    template_name = 'usuarios/perfil.html'

@login_required
def EditarPerfil(request):
    extradata = request.user.extradata
    formulario = FormEdicion(instance=request.user, initial={'avatar': extradata.avatar})
    
    if request.method == 'POST':
        formulario = FormEdicion(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            new_avatar = formulario.cleaned_data.get('avatar')
            extradata.avatar = new_avatar if new_avatar else extradata.avatar
            extradata.save()
            
            formulario.save()
            
            return redirect('inicio:home')
    
    return render(request, 'usuarios/editar_perfil.html', {'form': formulario})
    
class EditarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/password.html'
    success_url = reverse_lazy('usuarios:editar_perfil')
    