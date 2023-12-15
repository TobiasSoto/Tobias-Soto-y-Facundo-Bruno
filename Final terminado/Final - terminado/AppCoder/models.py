from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.camada}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    porfesion = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Entregable(models.Model):
    
    nombre =models.CharField(max_length=40)
    fechaDeEntrega =models.DateField()
    entregado = models.BooleanField()

class Libro(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    numerodeguardado = models.IntegerField()

    def __str__(self):
        return f'{self.nombre}'

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)