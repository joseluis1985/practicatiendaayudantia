from django import forms
from django.forms import ModelForm
from .models import *
import pdb
tipos=(('private','Privado'),('public','Publico'),('protected','Protegido'),)
class ProductoForm(ModelForm):
	class Meta:
		model=Producto

class PedidoForm(ModelForm):
	class Meta:
		model=Pedido