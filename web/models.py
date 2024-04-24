from django.db import models

# Create your models here.

class Especialidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField()

    class Meta:
        db_table = 'Especialidad'



class Medico(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)

    class Meta:
        db_table = 'Medico'