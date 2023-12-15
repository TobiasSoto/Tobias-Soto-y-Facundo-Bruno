from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.template import Template, Context, loader


def saludo(req):
    return HttpResponse("Hola a todos, esta es mi primer aplicacion con Django")

def segunda_vista(req):
    return HttpResponse(
        """
        <hl>Bienvenido a mi primer web</hl>
        <br>
        <br>
        <p>Esto esta muy bueno!</p>
        """
    )

def diaDeHoy(req):

    dia = datetime.now()
    documentoDeTexto = f"Hoy es:{dia}"
    return HttpResponse(documentoDeTexto)

def saluda_con_nombre(req, nombre):

    documentoDeTexto = f"Mi nombre es:{nombre}"
    return HttpResponse(documentoDeTexto)


def probando_template(req):
    
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render ({"my_name" : "nicolas", "notas" : [ 8, 9, 10, 3, 10, 8, 2, 1, 4, 9 ]})
    return HttpResponse(documento)
