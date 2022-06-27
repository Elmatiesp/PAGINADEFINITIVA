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
    img=models.ImageField(upload_to = 'web/static/web/img/',null=True,verbose_name='Imagen')
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre