from django import forms

class RopaFormBase(forms.Form):
    tipo = forms.CharField(max_length=15)
    marca = forms.CharField(max_length=15)
    talle = forms.CharField(max_length=15)    


class EditarRopaForm(RopaFormBase):...
    
class BuscarRopaForm(forms.Form):
    tipo = forms.CharField(max_length=15, required=False)