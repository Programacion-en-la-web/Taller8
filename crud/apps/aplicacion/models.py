from django.db import models

# Create your models here.

class tipodocumento(models.Model):
    id = models.IntegerField(primary_key= True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

class ciudad(models.Model):
    id = models.IntegerField()
    nombre = models.CharField(primary_key=True ,max_length=200)
    descripcion = models.CharField(max_length=200)

class persona(models.Model):
    id = models.IntegerField(primary_key= True)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    idtipodocumento = models.IntegerField()
    documento = models.CharField(max_length=200)
    lugarresidencia = models.CharField(max_length=200)
    fechanacimiento = models.DateField()
    email = models.CharField(max_length=200)
    telefono = models.IntegerField()
    usuario = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    idtipodocumento = models.ForeignKey(tipodocumento, on_delete=models.CASCADE)
    lugarresidencia = models.ForeignKey(ciudad, on_delete=models.CASCADE)

