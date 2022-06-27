from django.urls import path
from rest_mascotalandia.views import lista_producto, detalle_producto
from rest_mascotalandia.viewsLogin import login

urlpatterns = [
    path('lista_producto', lista_producto, name= "lista_producto"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
    path('login', login, name='login'),
]