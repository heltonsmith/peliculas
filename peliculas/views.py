from django.shortcuts import render, redirect
from .forms import PersonaForm
from .models import Pelicula

# Create your views here.
def home(request):
    pelicula_no_especiales = Pelicula.objects.filter(especial = False)
    return render(request, 'home.html', {'peliculas': pelicula_no_especiales})

def bienvenido(request):
    todas_peliculas = Pelicula.objects.all()
    return render(request, 'bienvenido.html', {'peliculas': todas_peliculas})


def registro(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.set_clave(form.cleaned_data['clave'])
            persona.save()
            return redirect('registro_exitoso')
    else:
        form = PersonaForm()
    return render(request, 'registro.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')

