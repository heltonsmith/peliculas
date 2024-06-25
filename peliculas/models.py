from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    anio_estreno = models.IntegerField()
    director = models.CharField(max_length=200)
    especial = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nombre
    
class Persona(models.Model):
    email = models.EmailField(primary_key=True)
    clave = models.CharField(max_length=128)
    nombre = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()

    def __str__(self) -> str:
        return self.nombre
    
    def set_clave(self, raw_password):
        self.clave = make_password(raw_password)

    def check_clave(self, raw_password):
        return check_password(raw_password, self.clave)