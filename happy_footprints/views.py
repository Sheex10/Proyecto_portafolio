from django.shortcuts import render, redirect, get_object_or_404

from .models import Producto, Categoria, Rol, Comment, User, Carrito
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CommentForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

# VISTAS PRINCIPALES

def home(request):
    return render(request, 'happy_footprints/home.html')

def Perros(request):
    listaProductos = Producto.objects.filter(categoria=4)
    contexto = {
        "productos" : listaProductos

    }
    return render(request, 'happy_footprints/Perros.html', contexto)


def Gatos(request):
    listaProductos = Producto.objects.filter(categoria=3)
    contexto = {
        "productos" : listaProductos

    }
    return render(request, 'happy_footprints/Gatos.html', contexto)



def Razas(request):
    return render(request, 'happy_footprints/Razas.html')

def Carrito(request):
    productos_en_carrito = []
    if 'carrito_productos' in request.session:
        lista_productos_id = request.session['carrito_productos']
        productos_en_carrito = Producto.objects.filter(id_producto__in=lista_productos_id)
    sumtotal = 0
    
    for i in productos_en_carrito:
        sumtotal += i.precio

    
    contexto={
        "productos":productos_en_carrito, 
        "suma":sumtotal, 
        
     
       
    }
    print(lista_productos_id)
    print(productos_en_carrito)
    return render(request, 'happy_footprints/Carrito.html',contexto)
   

def Preguntas(request):
    return render(request, 'happy_footprints/Preguntas.html')

#---------------------------------------------


#CRUD
@login_required
def Gestion(request):
    listadoCategorias = Categoria.objects.all()
    listadoProductos = Producto.objects.all()
    messages.success(request, '¡Productos listados!')
    return render(request, 'happy_footprints/Gestion.html', {"productos":listadoProductos, "categorias":listadoCategorias})


@login_required
def registrarProducto(request):
    id_producto = request.POST['txtID']
    nombre = request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    precio = request.POST['numPrecio']
    stock = request.POST['numStock']
    fotoP = request.FILES['ifoto']
    vCategoria = request.POST['Numcategorias']
    vRegCategoria = Categoria.objects.get(id_categoria=vCategoria)

    producto = Producto.objects.create(
        id_producto=id_producto, nombre=nombre, descripcion=descripcion, precio=precio, stock=stock, foto=fotoP, categoria=vRegCategoria)
    messages.success(request, '¡Producto registrado!')
    
    if vRegCategoria.id_categoria == 4:
        return redirect('Perros')
    if vRegCategoria.id_categoria == 3:
        return redirect('Gatos')

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


    producto = Producto.objects.get(id_producto=id_producto)
    producto.id_producto = id_producto
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.stock = stock

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

'''@login_required
def EditProducto(request):
    listaProductos = Producto.objects.all()
    contexto = {
        "nomProd": listaProductos

    }
    return render(request, 'happy_footprints/EditProducto.html', contexto)'''


def CamaPerro(request):

    return render(request, 'happy_footprints/CamaPerro.html')



def Produc(request):

    return render(request, 'happy_footprints/Produc.html')


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
    return redirect('login')


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

#----------------
@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comments')
    else:
        form = CommentForm()

    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'comments.html', {'form': form, 'comments': comments})


def comentarios(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comentarios')  # Cambia 'comments' por 'comentarios' si esa es la URL correcta
    else:
        form = CommentForm()

    tablaComentario = Comment.objects.all()
    

    context = {
        'tablaComentario': tablaComentario,
        'form' : form
    }
    return render(request, 'happy_footprints/comentarios.html', context)

#----------
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'happy_footprints/Produc.html', {'productos': productos})



def buscar_interno_producto(request, id):
    productos = Producto.objects.get(id_producto=id)
    contexto = {
        "producto": productos
    }
    return render(request, 'happy_footprints/CamaPerro.html', contexto)

def agregar_carrito(request, id):
    producto = Producto.objects.get(id_producto=id)
    usuario = User.objects.get(username=request.user.username)

    Carrito.objects.create(
        producto_carrito=producto,
        user_carrito=usuario,
        cantidad=1,
        precio_total=producto.precio
    )
    messages.success(request, "Producto agregado!.")
    return redirect('Carrito')

def agregar_carrito2(request, id):
    producto = Producto.objects.get(id_producto=id)
    usuario = User.objects.get(username=request.user.username)
    if 'carrito_productos' not in request.session:
        request.session['carrito_productos'] = []

    request.session['carrito_productos'].append(producto.id_producto)
    request.session.modified = True
    
    
    producto.stock=producto.stock-1
    producto.save()
    print('agregar carrito 2')
    
   
   
    messages.success(request, "Producto agregado!.")
    return redirect('buscar_interno_producto',id=id)

def eliminar_producto_carrito(request, id):
    if 'carrito_productos' in request.session:
        lista_productos_id = request.session['carrito_productos']
        
        # Convertir id a entero si es necesario
        id = int(id)
        
        if id in lista_productos_id:
            lista_productos_id.remove(id)
            request.session['carrito_productos'] = lista_productos_id
            request.session.modified = True
            
            # Obtener el producto y ajustar el stock
            producto = get_object_or_404(Producto, id_producto=id)
            producto.stock += 1
            producto.save()
            
            # Mensaje de éxito
            messages.success(request, "Producto eliminado del carrito.")
        else:
            print('No se encontró el id en la lista de carrito_productos:', id)
    else:
        print('No se encontró la lista de carrito_productos en la sesión.')
    
    return redirect('Carrito')