from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from web.models import Medico, Especialidad
from django.db.models import F

# Create your views here.
from django.shortcuts import render

def index(request):
    # Fetch the data from the database
    data = Especialidad.objects.all()

    # Pass the data to the template context
    context = {
        'data': data,
    }

    # Render the index.html template with the context
    return render(request, 'index.html', context)



def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'cobntact.html')

def medicos_especialidad(request):
    medicos = Medico.objects.all()
    especialidades = Especialidad.objects.all()

    # Add filters to the queryset based on request parameters
    if request.GET.get('especialidad'):
        medicos = medicos.filter(especialidad=request.GET.get('especialidad'))
    if request.GET.get('ciudad'):
        medicos = medicos.filter(ciudad=request.GET.get('ciudad'))

    # Annotate the queryset with the especialidad name
    medicos = medicos.annotate(especialidad_nombre=F('especialidad__nombre'))

    return render(request, 'medicos_especialidad.html', {'medicos': medicos, 'especialidades': especialidades})

def medico_detalle(request, medico_id):
    medico = Medico.objects.get(id=medico_id)
    return render(request, 'medico_detalle.html', {'medico': medico})