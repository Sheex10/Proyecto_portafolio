from django.urls import path
from core import views
from core.views import lista_usuario, detalle_usuario, lista_producto, detalle_producto
from core.viewslogin import login

urlpatterns = [
    path('lista_usuario',views.lista_usuario,name="lista_usuario"),
    path('detalle_usuario/<id>',views.detalle_usuario,name="detalle_usuario"),
    path('lista_producto',views.lista_producto,name="lista_producto"),
    path('detalle_producto',views.detalle_producto,name="detalle_producto"),
    path('login', login, name="login"),

]
