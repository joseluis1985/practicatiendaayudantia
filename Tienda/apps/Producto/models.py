from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import connection

class Producto(models.Model):
	Nombre=models.CharField(max_length=150)
	Descripcion=models.CharField(max_length=150)
	precio=models.FloatField(default=0)
	Stock=models.FloatField(default=0)

class Pedido(models.Model):
	Cliente=models.CharField(max_length=150)
	Producto=models.ManyToManyField(Producto)
	fecha=models.DateField(auto_now=True)
	Stock=models.IntegerField(default=0)
