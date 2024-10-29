from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from usuarios.forms import FormRegistro

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':    
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():

            usuario = formulario.get_user()
            django_login(request, usuario)
            
            return redirect('inicio:home')
    return render(request, 'usuarios/login.html', {'form': formulario})

def register(request):
    
    formulario = FormRegistro()
    if request.method == 'post':
        
        formulario = FormRegistro(request.post)
        if formulario.is_valid():
            
            formulario.save()
            return redirect('usuarios:login')
    
    return render(request, 'usuarios/register.html', {'form': formulario})