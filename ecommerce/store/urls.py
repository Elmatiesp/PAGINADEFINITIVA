from django.urls import path

from . import views
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

urlpatterns = [
        #Leave as empty string for base url
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('', views.principal, name="principal"),
    path('login/', views.login, name="login"),
    path('modificar/', views.modificar, name="modificar"),
    path('donacion/', views.donacion, name="donacion"),
    path('seguimiento/', views.seguimiento, name="seguimiento"),
    path('seguido/', views.seguido, name="seguido"),
    path('anadir/', views.anadir, name="anadir"),
    path('config/', views.config, name="config"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('config/<int:myname>/', views.eliminar, name="eliminar")


]