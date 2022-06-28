from ctypes import addressof
from multiprocessing import context
import re
from venv import create
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from django.shortcuts import redirect
import datetime
from . utils import cookieCart, cartData, guestOrder
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products':products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('El objeto se agrego', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)
            
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()  
      
    if order.shipping == True:
        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
        )
        
    return JsonResponse('Pago completado', safe=False)

def principal(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
    context = {'cartItems': cartItems}
    return render(request, 'store/principal.html', context)

def login(request):
        return render(request, 'store/login.html')

def modificar(request):
        return render(request, 'store/modificar.html')
    
def donacion(request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            cookieData = cookieCart(request)
            cartItems = cookieData['cartItems']
        context = {'cartItems': cartItems}
        return render(request, 'store/donacion.html', context)
    
def seguimiento(request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            cookieData = cookieCart(request)
            cartItems = cookieData['cartItems']
        context = {'cartItems': cartItems}
        return render(request, 'store/seguimiento.html', context)
    
def seguido(request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            cookieData = cookieCart(request)
            cartItems = cookieData['cartItems']
        context = {'cartItems': cartItems}
        return render(request, 'store/seguido.html', context)
    
def anadir(request):
    if request.method=="POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        digital = request.POST.get('digital')
        if digital == 'on':
            digital = True
        else:
            digital = False
        image = request.POST.get('image')
        producto = Product(name = name, price = price, digital = digital, image = image)
        producto.save()
        messages.info(request, "OBJETO AGREGADO CON EXITO")
    else:
        pass
    return render(request, 'store/anadir.html')

def eliminar(request, myname):
    item = Product.objects.get(price = myname)
    item.delete()
    return redirect(config)

def contacto(request):
    return render(request, 'store/contacto.html')

@login_required
def config(request):
    producto = Product.objects.all()
    context = {'productos' : producto}
    return render(request, 'store/config.html', context)
