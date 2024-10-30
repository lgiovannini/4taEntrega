from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre', max_length=20)
    last_name = forms.CharField(label='Apellido', max_length=20)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
  

class FormEdicion(UserChangeForm):
    password = None
    first_name = forms.CharField(label='Nombre', max_length=20)
    last_name = forms.CharField(label='Apellido', max_length=20)
    email = forms.EmailField(label='Correo', max_length=50)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'avatar']  
        