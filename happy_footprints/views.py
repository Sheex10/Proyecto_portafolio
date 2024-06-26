from django.shortcuts import render, redirect
from .models import Producto, Categoria, Rol
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

# VISTAS PRINCIPALES

def home(request):
    return render(request, 'happy_footprints/home.html')

def Perros(request):
    listaProductos = Producto.objects.filter(categoria=4)
    contexto = {
        "nomProd" : listaProductos

    }
    return render(request, 'happy_footprints/Perros.html', contexto)


def Gatos(request):
    listaProductos = Producto.objects.filter(categoria=3)
    contexto = {
        "nomProd" : listaProductos

    }
    return render(request, 'happy_footprints/Gatos.html', contexto)

def buscar_interno_producto(request, id):
    prod = Producto.objects.get(id_producto=id)
    contexto = {
        "nombree": prod
    }
    return render(request, 'happy_footprints/CamaPerro.html', contexto)

def Razas(request):
    return render(request, 'happy_footprints/Razas.html')

def Carrito(request):
    return render(request, 'happy_footprints/Carrito.html')

def Preguntas(request):
    return render(request, 'happy_footprints/Preguntas.html')

#---------------------------------------------


#CRUD
@login_required
def Gestion(request):
    listadoProductos = Producto.objects.all()
    messages.success(request, '¡Productos listados!')
    return render(request, 'happy_footprints/Gestion.html', {"productos":listadoProductos})
@login_required
def registrarProducto(request):
    id_producto = request.POST['txtID']
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['numPrecio']
    stock = request.POST['numStock']
    foto = request.POST['ifoto']

    producto = Producto.objects.create(
        id_producto=id_producto, nombre=nombre, descripcion=descripcion, precio=precio, stock=stock, foto=foto)
    messages.success(request, '¡Producto registrado!')
    return redirect('/')

@login_required
def edicionProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    return render(request, "happy_footprints/edicionProducto.html", {"producto": producto})
#??????????????
@login_required
def editarProducto(request):
    id_producto = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['numPrecio']
    stock = request.POST['numStock']
    foto = request.POST['ifoto']

    producto = Producto.objects.get(id_producto=id_producto)
    producto.id_producto = id_producto
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.stock = stock
    producto.foto = foto
    producto.save()

    messages.success(request, '¡Producto actualizado!')

    return redirect('/')

@login_required
def eliminarProducto(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    producto.delete()

    messages.success(request, '¡Producto eliminado!')

    return redirect('/')



#-------------------------------------------------------------------

@login_required
def EditProducto(request):
    listaProductos = Producto.objects.all()
    contexto = {
        "nomProd": listaProductos

    }
    return render(request, 'happy_footprints/EditProducto.html', contexto)


def CamaPerro(request):

    return render(request, 'happy_footprints/CamaPerro.html')



def Produc(request):

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



#????????
@login_required
def ControlProd(request):
    lista = Producto.objects.all()
    contexto = {
        "producto": lista
    }
    return render(request, 'happy_footprints/ControlProd.html', contexto)
#????????


@login_required
def ModiProd(request):
    vFotoProd = request.FILES.get('fotoProd', '')
    vIDProd = request.POST['idProd']
    vNombreProd = request.POST['nombreProd']
    vDescProd = request.POST['descripcionProd']
    vPrecioProd = request.POST['PrecioProd']
    vStockProd = request.POST['StockProd']
    vCategoriaProd = request.POST['categoriaProd']

    ProductoModi = Producto.objects.get(id_producto=vIDProd)
    ProductoModi.nombre = vNombreProd
    ProductoModi.descripcion = vDescProd
    ProductoModi.precio = vPrecioProd
    ProductoModi.stock = vStockProd

    registroCa = Categoria.objects.get(id_categoria=vCategoriaProd)
    ProductoModi.categoria = registroCa

    if vFotoProd != '':
        ProductoModi.foto = vFotoProd

    ProductoModi.save()
    messages.success(request, "Producto modificado.")
    return redirect('EditProducto')





#---------------------------------------------------------------






# VISTAS USUARIOS 
@login_required
def ModiPerfil(request):
    #datUsu = Usuario.objects.all()
    contexto = {
       # "usuarios": datUsu
    }
    return render(request, 'happy_footprints/ModiPerfil.html', contexto)

@login_required(login_url='InicioSesion')


#-------------------------------------------------------------
@login_required
def VerPerfil(request):
    #datUsuario = Usuario.objects.all()
    contexto = {
        #"usuarios": datUsuario

    }
    return render(request, 'happy_footprints/VerPerfil.html', contexto)


def exit(request):
    logout(request)
    return redirect('home')


#------------------------------------------------------------

def login(request):
    logout(request)
    
    return render(request, 'registration/login.html')
#---------------------------------------------------------

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request)
            return redirect('home')
        else:
            data['form'] = user_creation_form
    return render(request, 'happy_footprints/register.html', data)
    
#-------------------------------------------------------------

#PERROS

def CamasP(request):
    return render(request, 'Perros/CamasP.html')

def JuguetesP(request):
    return render(request, 'Perros/JuguetesP.html')

def CorreasP(request):
    return render(request, 'Perros/CorreasP.html')

def ComederosP(request):
    return render(request, 'Perros/ComederosP.html')

def CasasP(request):
    return render(request, 'Perros/CasasP.html')

#-------------------------------------------------------------

#GATOS

def CamasG(request):
    return render(request, 'Gatos/CamasG.html')

def JuguetesG(request):
    return render(request, 'Gatos/JuguetesG.html')

def CorreasG(request):
    return render(request, 'Gatos/CorreasG.html')

def ComederosG(request):
    return render(request, 'Gatos/ComederosG.html')

def CasasG(request):
    return render(request, 'Gatos/CasasG.html')  

