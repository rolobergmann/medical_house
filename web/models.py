from django.db import models
from django.contrib import admin
import uuid

# Create your models here.

class Especialidad(models.Model):
    id = models.CharField(max_length=5,primary_key=True)
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField()

    class Meta:
        db_table = 'Especialidad'

class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'descripcion')

# Create your models here.

class Medico(models.Model):
    rut = models.CharField(max_length=112, unique=True,primary_key=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=25)
    comuna = models.CharField(max_length=25)
    calle = models.CharField(max_length=25)
    numero = models.IntegerField()
    depto_casa = models.CharField(max_length=5)

    class Meta:
        db_table = 'Medico'

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('rut','nombre', 'apellido', 'especialidad_id', 'ciudad', 'comuna', 'calle', 'numero', 'depto_casa')


admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Medico, MedicoAdmin)

