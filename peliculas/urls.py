from django.urls import path
from .views import registro, registro_exitoso, home, bienvenido, login_view, logout_view

urlpatterns = [
    path("registro/", registro, name='registro'),
    path("registro_exitoso/", registro_exitoso, name='registro_exitoso'),
    path("home/", home, name='home'),
    path("login/", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path("bienvenido/", bienvenido, name='bienvenido'),
]
