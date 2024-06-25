from django.urls import path
from .views import registro, registro_exitoso, home, bienvenido

urlpatterns = [
    path("registro/", registro, name='registro'),
    path("registro_exitoso/", registro_exitoso, name='registro_exitoso'),
    path("home/", home, name='home'),
    path("bienvenido/", bienvenido, name='bienvenido'),
]
