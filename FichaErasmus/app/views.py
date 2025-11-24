from django.shortcuts import render
from .models import *
# Create your views here.

def principal(request):
    alumnos = Alumno.objects.all().order_by('apellidos', 'nombre')
    return render(request, 'app/principal.html', {'alumnos': alumnos})