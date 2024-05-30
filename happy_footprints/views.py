from django.shortcuts import render, redirect
from .models import Producto, Categoria, Rol
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

# Vistas principales

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

#---------------------------------------------

# Vistas para los productos


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

#---------------------------------------------------------------
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
    

def ControlProd(request):
    lista = Producto.objects.all()
    contexto = {
        "producto": lista
    }
    return render(request, 'happy_footprints/ControlProd.html', contexto)


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

#------------------------------------------------------------------
def formRegistro(request):
    vIdUser = request.POST['id_user']
    vNombre = request.POST['nomUser']
    vApellido = request.POST['apeUser']
    vClave = request.POST['Contrasena']
    vCorreo = request.POST['mailUser']
    vTelefono = request.POST['fonoUser']
    vRol = 2
    vRegistroRol = Rol.objects.get(nombreRol="usuario")
    print(f"aaaaaaaaaaa: {vRegistroRol}")
    #valida = Usuario.objects.all()
    #for xmail in valida:
    #    if xmail.correo == vCorreo:
    #        messages.error(request, "Este correo ya existe!")
    #        return redirect('Register')

    #Usuario.objects.create(id_usuario= vIdUser,nombre=vNombre, apellido=vApellido, clave=vClave, correo=vCorreo,telefono=vTelefono, rol=vRegistroRol)
    #user = User.objects.create_user(vCorreo, vCorreo, vClave)

    return redirect('InicioSesion')

#---------------------------------------------------------
@login_required
def ModiPerfil(request):
    #datUsu = Usuario.objects.all()
    contexto = {
       # "usuarios": datUsu
    }
    return render(request, 'happy_footprints/ModiPerfil.html', contexto)

@login_required(login_url='InicioSesion')

#----------------------------------------------------------------

def FormPerfilXD(request):
    vNombreUser = request.POST['nomUser']
    vApellidoUser = request.POST['apeUser']
    vCorreoUser = request.POST['correoUser']
    vFonoUser = request.POST['fonoUser']

    correoU = request.user.username
    #FormPerfilXD = Usuario.objects.get(correo=correoU)

    FormPerfilXD.nombre = vNombreUser
    FormPerfilXD.apellido = vApellidoUser
    FormPerfilXD.correo = vCorreoUser
    FormPerfilXD.telefono = vFonoUser
    FormPerfilXD.save()
    messages.success(request, "Perfil Modificado!.")

    return redirect('VerPerfil')


#------------------------------------------------
"""def InSesion(request):
    try:
        vCorreo = request.POST['correoUser']
        vClave = request.POST['password']
        vRol = 0
        vRun = 0
        registro = Usuario.objects.all()

        for i in registro:
            if i.correo == vCorreo and i.clave == vClave:

                vRun = i.id_usuario
                vRol = i.rol.id_rol
        user1 = User.objects.get(username=vCorreo)
        pass_valida = check_password(vClave, user1.password)

        if not pass_valida:
            messages.error(
                request, "El usuario o la contraseña son incorrectos")
            return redirect('InicioSesion')

        user = authenticate(username=vCorreo, password=vClave)

        if user is not None:
            if vRol == 2:
                login(request, user)
                return redirect('VerPerfil')

            if vRol == 1:
                login(request, user)
                return redirect('homeJefe')

            if vRol == 0:
                messages.success(request, "Usuario no registrado")
                return redirect('InicioSesion')
    except User.DoesNotExist:
        messages.error(request, "El usuario no existe")
        return redirect('InicioSesion')"""
#-------------------------------------------------------------
def VerPerfil(request):
    #datUsuario = Usuario.objects.all()
    contexto = {
        #"usuarios": datUsuario

    }
    return render(request, 'happy_footprints/VerPerfil.html', contexto)
    
#-------------------------------------------------------------
def Razas(request):
    return render(request, 'happy_footprints/Razas.html')

def Carrito(request):
    return render(request, 'happy_footprints/Carrito.html')

def Preguntas(request):
    return render(request, 'happy_footprints/Preguntas.html')

#-------------------------------------------------------------

#Perros

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

#Gatos

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

#------------------------------------------

def exit(request):
    logout(request)
    return redirect('home')


#------------------------------------------------------------

def login(request):
    logout(request)
    return render(request, 'registration/login.html')
#---------------------------

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
