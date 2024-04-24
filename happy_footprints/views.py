from django.shortcuts import render, redirect
from .models import Producto, Categoria
from django.contrib.auth.decorators import login_required


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


@login_required
def formProductos(request):
    vIdProd = request.POST['id']
    vDescripcion = request.POST['desc']
    vPrecio = request.POST['precio']
    vFoto = request.FILES['foto']
    vCategoria = request.POST['categoria']
    vStock = request.POST['stock']
    vNombre = request.POST['nombre']
    vRegCategoria = Categoria.objects.get(id_categoria=vCategoria)

    Producto.objects.create(nombre=vNombre, id_producto=vIdProd, descripcion=vDescripcion,
                            precio=vPrecio, foto=vFoto, categoria=vRegCategoria, stock=vStock)

    if vRegCategoria.id_categoria == 4:
        return redirect('Perros')
    if vRegCategoria.id_categoria == 3:
        return redirect('Gatos')