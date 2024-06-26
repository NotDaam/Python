from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import datetime

lista = [45, 30, 200]
def consultar(request, num):
    if num in lista:
        mensaje = "El Nro existe en la lista"
    else:
        mensaje = "El Nro no existe en la lista"

    return HttpResponse(mensaje)

def fecha_hora(request):
    now = datetime.datetime.now()
    html = "<h1>Hoy es %s. </h1>" % now
    return HttpResponse(html)

def plantilla_index(request):
    return render(request, 'index.html')

def plantilla_login(request):
    return render(request, 'login.html')