from django.http import HttpResponse
from django.shortcuts import render, redirect
from inicio.models import Ropa
from inicio.forms import BuscarRopaForm, EditarRopaForm
from django.views.generic.edit import CreateView, UpdateView ,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    return HttpResponse ('Blank')

class home(ListView):
    model = Ropa
    template_name = 'inicio/index.html'
    context_object_name = 'ropas'

def about(request):
    return render(request, 'inicio/about.html')

class CargarRopa(CreateView):
    model = Ropa
    template_name = "inicio/nueva_ropa.html"
    success_url = reverse_lazy('inicio:buscar_ropa')
    fields = ['tipo', 'marca', 'talle']


def buscar_ropa(request):
    
    formulario = BuscarRopaForm(request.GET)
    if formulario.is_valid():
        tipo = formulario.cleaned_data.get('tipo')
        ropas = Ropa.objects.filter(tipo__icontains=tipo)
        
    return render(request, 'inicio/buscar_ropa.html', {'ropas': ropas, 'form' : formulario})

class ver_ropa(DetailView):
    model = Ropa
    template_name = 'inicio/ver_ropa.html'

class eliminar_ropa(LoginRequiredMixin, DeleteView):
    model = Ropa
    template_name = 'inicio/eliminar.html'
    success_url = reverse_lazy('inicio:home')
    
class editar_ropa(LoginRequiredMixin, UpdateView):
    model = Ropa
    template_name = 'inicio/editar_ropa.html'
    success_url = reverse_lazy('inicio:buscar_ropa')
    fields = ['tipo', 'marca', 'talle']