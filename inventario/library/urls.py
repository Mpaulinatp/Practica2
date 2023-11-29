from django.urls import path
from . import views

urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('responsables', views.responsables, name='responsables'),
    path('inventario', views.inventario, name='inventario'),
    path('inventario/crear', views.crearIn, name='crear'),
    path('inventario/editar/<int:id>', views.editarIn, name='editar'),
    path('borrar/<int:id>', views.borrarIn, name='borrar'),
    path('responsable/crearRe', views.crearRe, name='crearRe'),
    

]