from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from happy_footprints.models import Usuario, Venta, Producto
from .serializers import UsuarioSerializers, ProductoSerializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_usuario(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializers(usuario,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_usuario(request, id):
    try:
        usuario = Usuario.objects.get(id_admin=id)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = usuario.Serializer(usuario)
        return Response(serializer.data)
    if request.method == 'PUT':
        date = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status)
    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NOT_CONTENT)

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_producto(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializers(producto,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_producto(request, id):

    try:
        producto = Producto.objects.get(id_admin=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Producto.Serializer(producto)
        return Response(serializer.data)
    if request.method == 'PUT':
        date = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NOT_CONTENT)

