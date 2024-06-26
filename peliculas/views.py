from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .forms import PersonaForm, PersonaLoginForm
from .models import Pelicula, Persona

# Create your views here.
def home(request):
    pelicula_no_especiales = Pelicula.objects.filter(especial = False)
    return render(request, 'home.html', {'peliculas': pelicula_no_especiales})

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

def bienvenido(request):
    todas_peliculas = Pelicula.objects.all()

    if 'persona_email' not in request.session:
        messages.error(request, 'Debes iniciar sesión para ver la página bienvenido!')
        return redirect('login')

    cuenta = request.session['persona_email']
    return render(request, 'bienvenido.html', {'peliculas': todas_peliculas, 'cuenta': cuenta})

def login_view(request):
    if request.method == 'POST':
        form = PersonaLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            clave = form.cleaned_data['clave']

            try:
                persona = Persona.objects.get(email=email)
                if persona.check_clave(clave):
                    request.session['persona_email'] = persona.email
                    return redirect('bienvenido')
                else:
                    form.add_error('clave', 'clave incorrecta')
            except Persona.DoesNotExist:
                form.add_error('email', 'correo no se encuentra registrado')
    else:
        form = PersonaLoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')