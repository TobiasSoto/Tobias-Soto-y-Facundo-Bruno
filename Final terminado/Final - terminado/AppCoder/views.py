
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Curso, Estudiante, Libro, Profesor, Avatar
from datetime import datetime
from django.template import Template, Context, loader
from .forms import FormularioCurso, FormularioEstudiante, FormularioLibros1, FormularioProfesor, RegisterFormulario,UserEditForm, AvatarFormulario
from django.views.generic import ListView
from django.views.generic import detail
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required










def sobremi(req):
    return render(req, "sobremi.html")


def inicio(req):

    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "inicio.html", {"url_avatar":avatar.imagen.url})
    except:
        return render(req, "inicio.html")

def cursos(req):

    return render(req, "cursos.html")

def profesores(req):

    return render(req, "profesores.html")

def entregables(req):

    return render(req, "entregables.html")

def estudiantes(req):

    return render(req, "estudiantes.html")



    
@staff_member_required(login_url='/app-coder/login')
def FormularioLibros(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
    
        miFormulario2 = FormularioLibros1(req.POST)

        if miFormulario2.is_valid():
            data=miFormulario2.cleaned_data
            libro=Libro(nombre=data["nombre"], precio=data["precio"], numerodeguardado=data["numerodeguardado"])
            libro.save()

            return render(req, "inicio.html")
    else:
        miFormulario2 =FormularioLibros1()
        return render(req, "formulariolibros.html",{"miFormulario2":miFormulario2})
    



class LibroDelete(DeleteView):
    model = Libro
    template_name = "libro_delete.html"
    success_url = '/app-coder/listaLibros'
    context_object_name = 'libro'



def login1(req):

    if req.method == 'POST':
    
        miFormulario = AuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():

            data=miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)
            if user:
                login(req, user)
                return render(req, "inicio.html",{"mensaje": f'Hola {usuario}!'})
        return render(req, "inicio.html",{"mensaje": f'Ingrese datos validos'})
    else:
        miFormulario =AuthenticationForm()
        return render(req, "login.html",{"miFormulario":miFormulario})
    

def register(req):

    if req.method == 'POST':
    
        miFormulario = RegisterFormulario(req.POST)

        if miFormulario.is_valid():

            data=miFormulario.cleaned_data
            usuario = data["username"]
            miFormulario.save()
            return render(req, "inicio.html",{"mensaje": f'{usuario} creado con exito!'})
        

        return render(req, "inicio.html",{"mensaje": f'Rellene los campos correctamente'})

    else:
        miFormulario =RegisterFormulario()
        return render(req, "registro.html",{"miFormulario":miFormulario})

def editar_perfil(req):
    usuario = req.user
    if req.method == 'POST':
    
        miFormulario = UserEditForm(req.POST, instance=req.user)

        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            usuario.fist_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render(req, "inicio.html", {"mensaje": "Datos actualizados con exito!"})
        else:
            return render(req, "editarperfil.html",{"miFormulario":miFormulario})           
    else:
        miFormulario =UserEditForm(instance=usuario)
        return render(req, "editarperfil.html",{"miFormulario":miFormulario})

class LibroList(LoginRequiredMixin, ListView):
    model = Libro
    template_name = "libro_list.html"
    context_object_name = "libros"

class LibroDetail(DetailView):
    model=Libro
    template_name = "libro_detail.html"
    context_object_name = "libro"



def agregar_avatar(req):

    if req.method == 'POST':
    
        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            avatar = Avatar(user=req.user, imagen=data["imagen"])
            avatar.save()

            return render(req, "inicio.html", {"mensaje": "Avatar actualizado con exito!"})
        else:
            return render(req, "editarperfil.html",{"miFormulario":miFormulario})           
    else:
        miFormulario =AvatarFormulario()
        return render(req, "agregarAvatar.html",{"miFormulario":miFormulario})
    

@login_required
def BusquedaLibro(req):
    return render(req, "busquedalibro.html")

def buscarlibro(req: HttpRequest):
    if "numerodeguardado" in req.GET:
        try:
            numerodeguardado = req.GET["numerodeguardado"]
        except ValueError:
            return HttpResponse("Ingrese un numero de guardado válido")

        try:
            libro = Libro.objects.get(numerodeguardado=numerodeguardado)
            return render(req, "resultadobuscarlibro.html", {"libro": libro})
        except Libro.DoesNotExist:
            return HttpResponse(f"No se encontró un libro con ese numero de guardado '{numerodeguardado}'")
        except ValueError:
            return HttpResponse("Ingrese un numero de guardado válido")
    else:
        return HttpResponse("Debe agregar un numero de guardado en la consulta")   
    
@staff_member_required(login_url='/app-coder/login')
def editarLibros(req, id):
    libro = Libro.objects.get(id=id)
    if req.method == 'POST':
    
        miFormulario = FormularioLibros1(req.POST)

        if miFormulario.is_valid():

            data=miFormulario.cleaned_data
            libro.nombre = data["nombre"]
            libro.precio = data["precio"]
            libro.numerodeguardado = data["numerodeguardado"]
            libro.save()

            return render(req, "inicio.html")
    else:
        miFormulario =FormularioLibros1(initial={
            "nombre": libro.nombre,
            "precio" : libro.precio,
            "numerodeguardado": libro.numerodeguardado,
        })
        return render(req, "editarlibros.html",{"miFormulario":miFormulario, "id": libro.id})


@staff_member_required(login_url='/app-coder/login')
def eliminarLibro(req, id):

    if req.method == 'POST' :
        libro = Libro.objects.get(id=id)
        libro.delete()

        libros = Libro.objects.all()

        return render(req, "libro_list.html", {"libros": libros})