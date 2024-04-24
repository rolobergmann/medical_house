from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from web.models import Medico, Especialidad

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