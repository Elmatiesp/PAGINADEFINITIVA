from msilib.schema import Class
from pyexpat import model
from django.db import models

#modelo para categoria
class Marca(models.Model):
    nombre= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
class Producto(models.Model):
    nombre = models.CharField(max_length=55)
    precio = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre