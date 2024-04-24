from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.
def home(request):
    return render(request, 'happy_footprints/home.html')

def Perros(request):
    listaProductos = Producto.objects.filter(categoria=1)
    contexto = {
        "nombreProd" : listaProductos

    }
    return render(request, 'happy_footprints/Perros.html', contexto)


def Gatos(request):
    listaProductos = Producto.objects.filter(categoria=2)
    contexto = {
        "nombreProd" : listaProductos

    }
    return render(request, 'happy_footprints/Gatos.html', contexto)

def buscar_interno_producto(request, id):
    prod = Producto.objects.get(id_producto=id)
    contexto = {
        "nombree": prod
    }
    return render(request, 'happy_footprints/CamaPerro.html', contexto)

def Producto(request):

    return render(request, 'happy_footprints/Producto.html')