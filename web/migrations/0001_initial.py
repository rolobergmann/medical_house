# Generated by Django 5.0.4 on 2024-04-25 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.CharField(editable=False, max_length=5, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'Especialidad',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('rut', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('ciudad', models.CharField(default='sin ciudad', max_length=25)),
                ('comuna', models.CharField(blank=True, default='sin comuna', max_length=25, null=True)),
                ('calle', models.CharField(default='sin calle', max_length=25)),
                ('numero', models.IntegerField(default=0)),
                ('depto_casa', models.CharField(max_length=5, null=True)),
                ('fecha_nac', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('rut', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('ciudad', models.CharField(default='sin ciudad', max_length=25)),
                ('comuna', models.CharField(blank=True, default='sin comuna', max_length=25, null=True)),
                ('calle', models.CharField(default='sin calle', max_length=25)),
                ('numero', models.IntegerField(default=0)),
                ('depto_casa', models.CharField(max_length=5, null=True)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.especialidad')),
            ],
            options={
                'db_table': 'Medico',
            },
        ),
    ]
