import imp
from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.

def home(request):
    return render(request, 'web/index.html')

def index(request):
    return render(request, 'web/index.html')

def productos(request):
    return render(request, 'web/productos.html')

def seguimiento(request):
    return render(request, 'web/seguimiento.html')

def donacion(request):
    return render(request, 'web/donacion.html')

def contacto(request):
    return render(request, 'web/contacto.html')

def seguido(request):
    return render(request, 'web/seguido.html')

def BD(request):
    producto = Producto.objects.all()
    data = {
            'producto':producto
    }
    return render(request, 'web/BD.html',data)

def adm(request):
    return render(request, 'web/adm.html')

def crearpro(request):
    return render(request, 'web/crearpro.html')

