from django.db import models
from django.contrib import admin
import uuid
from django.contrib import admin
import uuid

# Create your models here.

class Especialidad(models.Model):
    id = models.CharField(max_length=5,primary_key=True,unique=True,editable=False)

    nombre = models.CharField(max_length=25)
    descripcion = models.TextField()

    class Meta:
        db_table = 'Especialidad'

class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'descripcion')
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'descripcion')

# Create your models here.
# Create your models here.

class Medico(models.Model):
    rut = models.CharField(max_length=11, unique=True,primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=25, null=False ,blank=False, default='sin ciudad')
    comuna = models.CharField(max_length=25, null=True, blank=True, default='sin comuna')
    calle = models.CharField(max_length=25, null=False ,blank=False, default='sin calle')
    numero = models.IntegerField(default=0)
    depto_casa = models.CharField(max_length=5, null=True)

    class Meta:
        db_table = 'Medico'

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('rut','nombre', 'apellido', 'especialidad_id', 'ciudad', 'comuna', 'calle', 'numero', 'depto_casa')
    list_filter = ('ciudad', 'comuna')

admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Medico, MedicoAdmin)

class Paciente(models.Model):
    rut = models.CharField(max_length=11,primary_key=True,unique=True)
    nombre = models.CharField(max_length=25, default='sin nombre')
    apellido = models.CharField(max_length=25)
    ciudad = models.CharField(max_length=25, null=False ,blank=False, default='sin ciudad')
    comuna = models.CharField(max_length=25, null=True, blank=True, default='sin comuna')
    calle = models.CharField(max_length=25, null=False ,blank=False, default='sin calle')
    numero = models.IntegerField(default=0)
    depto_casa = models.CharField(max_length=5, null=True)
    fecha_nac = models.DateField(null=True, blank=True)
    class Meta:
            db_table = 'Paciente'

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('rut','nombre', 'apellido', 'ciudad', 'comuna', 'calle', 'numero', 'depto_casa', 'fecha_nac')
    list_filter = ('ciudad', 'comuna')
    search_fields = ['rut', 'ciudad', 'apellido']

admin.site.register(Paciente, PacienteAdmin)