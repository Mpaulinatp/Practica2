from django import forms
from .models import Respons
from .models import Invent
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *


class ResponsForm(forms.ModelForm):
    class Meta:
        model= Respons
        fields= '_all_'
    

class InventForm(forms.ModelForm):
        class Meta:
            model= Invent
            fields= '_all_'


class UserLoginForm(AuthenticationForm):
    def _init_(self, *args, **kwargs):
        super(UserLoginForm, self)._init_(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Correo electrónico', 'autocomplete': 'off'}),
        label="Correo electrónico")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'autocomplete': 'off'}),
        label="Contraseña")