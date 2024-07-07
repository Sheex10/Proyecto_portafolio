from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#-------------------------------------

class Rol(models.Model):
    id_rol=models.IntegerField(primary_key=True, verbose_name="id de rol")
    nombreRol=models.CharField(max_length=30, verbose_name="nombre del rol")
    
    def __str__(self):
        return self.nombreRol

#-----------------------------------------------------------------------

class Categoria(models.Model):
    id_categoria=models.IntegerField(primary_key=True, verbose_name="id de rol")
    nombre=models.CharField(max_length=30, verbose_name="nombre de categoria")
    
    def __str__(self):
        return self.nombre
    
#--------------------------------------
class Producto(models.Model):
    id_producto =models.IntegerField(primary_key=True, verbose_name="id del producto")
    nombre=models.CharField(max_length=30, verbose_name="nombre del producto")
    descripcion=models.CharField(max_length=700, verbose_name="descripcion producto")
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.IntegerField()
    foto=models.ImageField(upload_to="foto producto")
    categoria =models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
#---------------------------------------

#----------------------------------------------
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.created_at}'

#--------------MODELOS PARA EL CARRITO------------
class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True, verbose_name="id del carrito")
    producto_carrito = models.ForeignKey(Producto, on_delete=models.CASCADE)
    user_carrito = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name="cantidad del producto")
    precio_total = models.IntegerField(verbose_name="total del carrito")

    def __str__(self):
        return self.producto_carrito
