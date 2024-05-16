from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    consulta =models.Producto.objects.all()
    contexto = {'productos':consulta}
    return render(request,'Almacen/index.html', contexto)