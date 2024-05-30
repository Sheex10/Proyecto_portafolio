from django.contrib import admin
from .models import Rol, Categoria, Producto, Direccion
# Register your models here.

admin.site.register(Rol)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Direccion)
