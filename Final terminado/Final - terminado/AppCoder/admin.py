from django.contrib import admin
from .models import Curso, Profesor, Estudiante, Entregable, Libro, Avatar, Profile
# Register your models here.
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)
admin.site.register(Libro)
admin.site.register(Avatar)
admin.site.register(Profile)