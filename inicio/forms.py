from django import forms

class RopaFormBase(forms.Form):
    tipo = forms.CharField(max_length=15)
    marca = forms.CharField(max_length=15)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    descripcion = forms.CharField(max_length=200)


class EditarRopaForm(RopaFormBase):...
    
class BuscarRopaForm(forms.Form):
    tipo = forms.CharField(max_length=15, required=False)