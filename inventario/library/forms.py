from django import forms
from .models import Respons
from .models import Invent

class ResponsForm(forms.ModelForm):
    class Meta:
        model= Respons
        fields= '__all__'
    

class InventForm(forms.ModelForm):
        class Meta:
            model= Invent
            fields= '__all__'