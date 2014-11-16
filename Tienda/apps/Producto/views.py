from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect 
import datetime
from .forms import *
from .models import *

import pdb
# Create your views here.
def registro_view(request):
	if(request.method=="POST"):
		form=ProductoForm(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect("/Producto/registro/")
	form=ProductoForm()	
	return render_to_response("Producto/registro.html",{"form":form},RequestContext(request))
def inicio_view(request):
	return render_to_response("Producto/inicio.html",{},context_instance=RequestContext(request))
def pedidos_view(request):
	if(request.method=="POST"):
		form=PedidoForm(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect("/Producto/pedidos/")
	form=PedidoForm()	
	return render_to_response("Producto/pedidos.html",{"form":form},RequestContext(request))