from dataclasses import fields
from django import forms
from django.forms import ModelForm
from web.models import Producto 

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'img', 'descripcion']
