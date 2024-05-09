from django.urls import path
from happy_footprints import views
from .views import home, Gatos, Perros, buscar_interno_producto, Produc, VerPerfil,formProductos, EditProducto, ModiProd, formRegistro, ModiPerfil, FormPerfilXD, InSesion, InicioSesion, Razas, CamaPerro, ControlProd, Carrito


urlpatterns = [
    path('', home, name="home"),
    path('Gatos', Gatos,name="Gatos"),
    path('Perros', Perros,name='Perros'),
    path('buscar_interno_producto/<int:id>',buscar_interno_producto,name="buscar_interno_producto"),
    path('Produc', Produc, name="Produc"),
    path('VerPerfil', VerPerfil, name="VerPerfil"),
    path('formProductos', formProductos, name="formProductos"),
    path('EditProducto', EditProducto, name="EditProducto"),
    path('ModiProd', ModiProd, name="ModiProd"),
    path('formRegistro', formRegistro, name="formRegistro"),
    path('ModiPerfil', ModiPerfil, name="ModiPerfil"),
    path('FormPerfilXD', FormPerfilXD, name="FormPerfilXD"),
    path('InSesion', InSesion, name="InSesion"),
    path('InicioSesion', InicioSesion,name="InicioSesion"),
    path('Razas', Razas,name="Razas"),
    path('CamaPerro', CamaPerro,name="CamaPerro"),
    path('ControlProd',ControlProd,name="ControlProd"),
    path('home', views.home, name='home'),
    path('Carrito', Carrito, name="Carrito"),


]