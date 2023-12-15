from django.urls import path
from .views import  *
from django.contrib import admin
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name="inicio"),
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name="profesores"),
    path('entregables/', entregables, name="entregables"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('FormularioLibros/', FormularioLibros, name="FormularioLibros"),
    path('login/', login1, name="Login"),
    #path('admin/', admin.site.urls),
    path('register/', register , name="Register"),
    path('logout/', LogoutView.as_view(template_name= "logout.html"), name="logout"),
    path('editarperfil/', editar_perfil, name="EditarPerfil"),
    path('listaLibros/', LibroList.as_view(), name="ListaLibros"),
    path('Eliminarlibros/<pk>', LibroDelete.as_view(), name="EliminarLibros"),
    path('EspicificacionesLibros/<pk>', LibroDetail.as_view(), name="EspicificacionesLibros"),
    path('AgregarAvatar/', agregar_avatar , name="AgregarAvatar"),
    path('buscarlibro/',buscarlibro , name="BuscarLibro"),
    path('BusquedaLibros/', BusquedaLibro , name="BusquedaLibros"),
    path('sobremi/', sobremi, name="SobreMi"),
    path('editarLibros/<int:id>', editarLibros, name="EditarLibros"),
    path('eliminaLibros/<int:id>', eliminarLibro, name="EliminaLibros"),


    

    ]