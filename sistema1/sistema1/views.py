from django.http import HttpResponse
import os

def saludar(request):
    mensaje = "Hola hola, estamos probando:)"
    return HttpResponse(mensaje)