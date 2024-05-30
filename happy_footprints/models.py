from django.db import models

# Create your models here.

#-------------------------------------

class Rol(models.Model):
    id_rol=models.IntegerField(primary_key=True, verbose_name="id de rol")
    nombreRol=models.CharField(max_length=30, verbose_name="nombre del rol")
    
    def __str__(self):
        return self.nombreRol

#-----------------------------------------------------------------------

#----------------------------------
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
    precio=models.IntegerField(verbose_name="precio producto")
    stock = models.IntegerField()
    foto=models.ImageField(upload_to="foto producto")
    categoria =models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
#---------------------------------------
class Direccion(models.Model):
    id_direccion =models.IntegerField(primary_key=True, verbose_name="id de direccion")
    calle=models.CharField(max_length=100, verbose_name="nombre calle")
    numero=models.IntegerField(verbose_name="numero casa")
    descripcion=models.CharField(max_length=600, verbose_name="descripcion direccion")
    
    
    def __str__(self):
        return self.descripcion
#----------------------------------------------

