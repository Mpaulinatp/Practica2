from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Invent
from .models import Respons
from .forms import ResponsForm
from .forms import InventForm

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
    infoResponsable=ResponsForm(request.POST or None)
    if infoResponsable.is_valid():
        infoResponsable.save()
        return redirect('responsables')
    return render(request, 'responsables/crear.html')

