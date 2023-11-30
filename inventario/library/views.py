from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Invent
from .models import Respons
from .forms import ResponsForm
from .forms import InventForm
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', '') 
                return redirect('inicio')
            else:
                return render(request=request, template_name="registro/login.html", context={'form': form})
        else:
            for key, error in list(form.errors.items()):
                messages.error(request, error)
    form = UserLoginForm()
    return render(request=request, template_name="registro/login.html", context={'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') 

@login_required
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

@login_required
def responsables(request):
    responsables = Respons.objects.all()
    return render(request, 'responsables/listar.html', {'responsables':responsables})

@login_required
def inventario(request):
    equipos = Invent.objects.all()
    return render(request, 'inventario/listarIn.html', { 'equipos':equipos})

@login_required
def archivos(request):
    equipos_biomedica = Invent.objects.filter(area='Biomédica')
    equipos_infraestructura = Invent.objects.filter(area='Infraestructura')
    equipos_sistemas = Invent.objects.filter(area='Sistemas')
    equipos = Invent.objects.all()

    context = {
        'equipos_biomedica': equipos_biomedica,
        'equipos_infraestructura': equipos_infraestructura,
        'equipos_sistemas': equipos_sistemas,
        'equipos':equipos
    }
   
    return render(request, 'consultar/activos.html', context)

@login_required
def crearIn(request):
    infoActivo=InventForm(request.POST or None)
    if infoActivo.is_valid():
        infoActivo.save()
        return redirect('inventario')
    responsables = Respons.objects.all()
    return render(request, 'inventario/crearIn.html', {'responsables':responsables})

@login_required
def borrarIn(request, id):
    equipo =Invent.objects.get(id=id)
    equipo.delete()
    return redirect('inventario')

@login_required
def  editarIn(request,id):
    inventario=Invent.objects.get(id=id)
    formInvent=InventForm(request.POST or None , instance=inventario)
    responsabless = Respons.objects.all()
    if formInvent.is_valid() and request.method == 'POST':
        formInvent.save()
        return redirect('inventario')
    return render(request, 'inventario/editarIn.html', {'formInvent':formInvent, 'responsabless':responsabless})

@login_required
def crearRe(request):
    infoResponsable=ResponsForm(request.POST or None)
    if infoResponsable.is_valid():
        infoResponsable.save()
        return redirect('responsables')
    return render(request, 'responsables/crear.html')

