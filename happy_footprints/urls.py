from django.urls import path
from happy_footprints import views
from .views import home, Gatos, Perros, buscar_interno_producto, Produc,agregar_carrito, VerPerfil,formProductos, ModiPerfil, login, Razas, CamaPerro, ControlProd, Carrito, Preguntas, CamasP, CasasP, ComederosP, CorreasP, JuguetesP, CamasG, CasasG, ComederosG, CorreasG, CorreasG, JuguetesG, exit, register, Gestion, add_comment, comentarios


urlpatterns = [
    path('', home, name="home"),
    path('Gatos', Gatos,name="Gatos"),
    path('Perros', Perros,name='Perros'),
    path('buscar_interno_producto/<int:id>',buscar_interno_producto,name="buscar_interno_producto"),
    path('Produc', Produc, name="Produc"),
    path('VerPerfil', VerPerfil, name="VerPerfil"),
    path('formProductos', formProductos, name="formProductos"),
    path('ModiPerfil', ModiPerfil, name="ModiPerfil"),
    path('login/', login,name="login"),
    path('Razas', Razas,name="Razas"),
    path('CamaPerro', CamaPerro,name="CamaPerro"),
    path('ControlProd',ControlProd,name="ControlProd"),
    path('home', views.home, name='home'),
    path('Carrito', Carrito, name="Carrito"),
    path('Preguntas', Preguntas, name="Preguntas"),
    path('CamasP', CamasP, name="CamasP"),
    path('CasasP', CasasP, name="CasasP"),
    path('ComederosP', ComederosP, name="ComederosP"),
    path('CorreasP', CorreasP, name="CorreasP"),
    path('JuguetesP', JuguetesP, name="JuguetesP"),
    path('CamasG', CamasG, name="CamasG"),
    path('CasasG', CasasG, name="CasasG"),
    path('ComederosG', ComederosG, name="ComederosG"),
    path('CorreasG', CorreasG, name="CorreasG"),
    path('JuguetesG', JuguetesG, name="JuguetesG"),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('Gestion', Gestion, name="Gestion"),
    path('eliminarProducto/<id_producto>', views.eliminarProducto),
    path('editarProducto/', views.editarProducto),
    path('edicionProducto/<id_producto>', views.edicionProducto),
    path('registrarProducto', views.registrarProducto),
    path('comments', add_comment, name='comments'),
    path('comentarios', comentarios, name='comentarios'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('agregar_carrito/<id>', agregar_carrito, name="agregar_carrito"),

]

