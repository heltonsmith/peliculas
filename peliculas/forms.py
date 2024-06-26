from django import forms 
from .models import Persona 


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['email', 'clave', 'nombre', 'fecha_nacimiento']
        widgets = {
            'clave': forms.PasswordInput(),
        }

class PersonaLoginForm(forms.Form):
    email = forms.EmailField()
    clave = forms.CharField(widget=forms.PasswordInput)