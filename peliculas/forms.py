from django import forms 
from .models import Persona 


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['email', 'clave', 'nombre', 'fecha_nacimiento']
        widgets = {
            'clave': forms.PasswordInput(),
        }