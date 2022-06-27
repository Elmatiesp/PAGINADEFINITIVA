import imp
from django.shortcuts import render, redirect
from .models import Producto
from web.forms import ProductoForm

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

def Productolista(request):
    producto = Producto.objects.all()
    data = {
            'producto':producto
    }
    return render(request, 'web/Productolista.html',data)

def Form_Producto(request):
    datos = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST or None, request.FILES or None)

        if formulario.is_valid():
            formulario.save() #insert a la BD
            datos['mensaje'] = 'Se guardó el producto'
        else:
            datos['mensaje'] = 'NO se guardó el producto'
 
    return render(request,"web/Form_Producto.html", datos)

def Modificar_Producto(request, id):
    producto = Producto.objects.get(nombre = id)

    datos = {
        'form': ProductoForm(instance = producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST or None, request.FILES or None, instance = producto)

        if formulario.is_valid():
            formulario.save() #modificar a la BD
            datos['mensaje'] = 'Se modificó el plato'
        else:
            datos['mensaje'] = 'NO se modificó el plato'

    return render(request,"Polls/Modificar_Producto.html", datos)

def Eliminar_Producto(request, id):
    producto = Producto.objects.get(nombre = id)
    producto.delete() #delete de la BD
    return redirect(to='Productolista')


def adm(request):
    return render(request, 'web/adm.html')

def iniciosesion(request):
    return render(request, 'web/iniciosesion.html')

def crearpro(request):
    return render(request, 'web/crearpro.html')

