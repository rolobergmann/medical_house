# Generated by Django 5.0.4 on 2024-04-25 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_paciente_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='nombre',
            field=models.CharField(default='sin nombre', max_length=25),
        ),
    ]