from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Invent
from .models import Respons
from .forms import ResponsForm
from .forms import InventForm

def inicio(request):
    equipos = Invent.objects.all()
    total_equipos = equipos.count()

    biomedica_count = equipos.filter(area='Biomédica').count()
    infraestructura_count = equipos.filter(area='Infraestructura').count()
    sistemas_count = equipos.filter(area='Sistemas').count()

    # Calcula el porcentaje antes de pasarlos a la plantilla
    porcentaje_biomedica = 0 if total_equipos == 0 else (biomedica_count / total_equipos) * 100
    porcentaje_infraestructura = 0 if total_equipos == 0 else (infraestructura_count / total_equipos) * 100
    porcentaje_sistemas = 0 if total_equipos == 0 else (sistemas_count / total_equipos) * 100

    return render(request, 'paginas/index.html', {
        'equipos': equipos,
        'total_equipos': total_equipos,
        'biomedica_count': biomedica_count,
        'infraestructura_count': infraestructura_count,
        'sistemas_count': sistemas_count,
        'porcentaje_biomedica': porcentaje_biomedica,
        'porcentaje_infraestructura': porcentaje_infraestructura,
        'porcentaje_sistemas': porcentaje_sistemas,
    })



def responsables(request):
    responsables = Respons.objects.all()
    return render(request, 'responsables/listar.html', {'responsables':responsables})


def inventario(request):
    equipos = Invent.objects.all()
    return render(request, 'inventario/listarIn.html', { 'equipos':equipos})

def crearIn(request):
    infoActivo=InventForm(request.POST or None)
    if infoActivo.is_valid():
        infoActivo.save()
        return redirect('inventario')
    responsables = Respons.objects.all()
    return render(request, 'inventario/crearIn.html', {'responsables':responsables})

def borrarIn(request, id):
    equipo =Invent.objects.get(id=id)
    equipo.delete()
    return redirect('inventario')

def  editarIn(request,id):
    inventario=Invent.objects.get(id=id)
    formInvent=InventForm(request.POST or None , instance=inventario)
    responsabless = Respons.objects.all()
    if formInvent.is_valid() and request.method == 'POST':
        formInvent.save()
        return redirect('inventario')
    return render(request, 'inventario/editarIn.html', {'formInvent':formInvent, 'responsabless':responsabless})

def crearRe(request):
    infoResponsable=ResponsForm(request.POST or None)
    if infoResponsable.is_valid():
        infoResponsable.save()
        return redirect('responsables')
    return render(request, 'responsables/crear.html')

