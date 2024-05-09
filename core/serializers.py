from rest_framework import serializers
from happy_footprints.models import Usuario, Producto

#clase de usuario

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario','nombre','apellido','correo','clave','telefono','rol']

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id_producto','nombre','descripcion','precio','stock','categoria']
    