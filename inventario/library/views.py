from django.shortcuts import render
from django.http import HttpResponse
from .models import Invent
from .models import Respons
# Create your views here.

def inicio(request):
    return render(request, 'paginas/index.html')


def responsables(request):
    responsables = Respons.objects.all()
    return render(request, 'responsables/listar.html', {'responsables':responsables})


def inventario(request):
    equipos = Invent.objects.all()
    return render(request, 'inventario/listarIn.html', { 'equipos':equipos})

def crearIn(request):
    return render(request, 'inventario/crearIn.html')

def borrarIn(request):
    return render(request, 'inventario/borrarIn.html')

def  editarIn(request):
    return render(request, 'inventario/editarIn.html')

def crearRe(request):
    return render(request, 'responsables/crear.html')

