from django.urls import path
from happy_footprints import views
from .views import home, Gatos, Perros, buscar_interno_producto, Producto



urlpatterns = [
    path('', home, name="home"),
    path('Gatos', Gatos,name="Gatos"),
    path('Perros', Perros,name='Perros'),
    path('buscar_interno_producto/<int:id>',buscar_interno_producto,name="buscar_interno_producto"),
    path('Producto', Producto, name="Producto"),
]