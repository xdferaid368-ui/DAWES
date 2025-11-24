from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def principal(request):
    alumnos = Alumno.objects.all().order_by('apellidos', 'nombre')
    return render(request, 'app/principal.html', {'alumnos': alumnos})

def detalle_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    return render(request, 'app/detalle_alumno.html', {'alumno': alumno})