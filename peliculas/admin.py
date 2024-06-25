from django.contrib import admin
from .models import Pelicula, Persona

# Register your models here.
@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'anio_estreno', 'director', 'especial')
    search_fields = ('nombre', 'director')
    list_filter = ('anio_estreno', 'especial')


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombre', 'fecha_nacimiento')
    search_fields = ('email', 'nombre')
