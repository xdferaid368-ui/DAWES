from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
# Create your views here.

def principal(request):
    alumnos = Alumno.objects.all().order_by('apellidos', 'nombre')
    return render(request, 'app/principal.html', {'alumnos': alumnos})

def detalle_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    return render(request, 'app/detalle_alumno.html', {'alumno': alumno})


def crear_ficha(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal')
    else:
        form = AlumnoForm()
    return render(request, 'app/crear_ficha.html', {'form': form})

def eliminar_ficha(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('principal')
    return render(request, 'app/eliminar_ficha.html', {'alumno': alumno})

def editar_ficha(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('principal')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'app/editar_ficha.html', {'form': form, 'alumno': alumno})