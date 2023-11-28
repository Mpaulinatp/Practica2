from django.db import models

# Create your models here.
#Permite crear una tabla para inventario, así mismo la de responsables
class Invent(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.TextField(max_length=80)
    marca=models.TextField(max_length=80)
    modelo=models.TextField(max_length=80)
    serial=models.TextField(max_length=80)
    area=models.TextField(max_length=80)
    responsable=models.TextField(max_length=80)

class Respons(models.Model):
    id=models.AutoField(primary_key=True)
    documento=models.TextField(max_length=80)
    nombre=models.TextField(max_length=80)
    apellido=models.TextField(max_length=80, default='')
    correo=models.EmailField(max_length=254)