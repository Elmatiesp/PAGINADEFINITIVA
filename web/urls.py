from django.urls import path
from .views import home, productos, index, seguimiento, donacion, contacto, seguido, BD, adm, crearpro

urlpatterns = [
    path('', home, name="home"),
    path('index' , index, name="index"),
    path('productos', productos, name="productos"),
    path('seguimiento', seguimiento, name="seguimiento"),
    path('donacion', donacion, name="donacion"),
    path('contacto', contacto, name="contacto"),
    path('seguido', seguido, name="seguido"),
    path('BD', BD, name="BD"),
    path('adm', adm, name="adm"),
    path('crearpro', crearpro, name="crearpro"),
]