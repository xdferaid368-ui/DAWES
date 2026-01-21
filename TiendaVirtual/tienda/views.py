from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from .forms import *
# Create your views here.

class Inicio(TemplateView):
    template_name = "tienda/inicio.html"
    
class ListadoProductos(ListView):
    model = Producto
    template_name = 'tienda/listadoProductos.html'
    context_object_name = 'productos'
class EditarProducto(UpdateView):
    model = Producto
    form_class= ProductoEditarForm
    template_name = 'tienda/productoeditar.html'
    success_url = reverse_lazy('listadoProductos')
    
class EliminarProducto(DeleteView):
    model = Producto
    template_name = 'tienda/eliminarProducto.html'
    success_url = reverse_lazy('listadoProductos')

class CrearProducto(CreateView):
    model = Producto
    template_name = 'tienda/crearProducto.html'
    fields = ['nombre','modelo','unidades','precio','vip','marca' ]
    success_url = reverse_lazy('listadoProductos')

def listado_productos_compra(request):
    productos = list(Producto.objects.all()) 
    buscar = request.GET.get('buscar', '').lower()
    vip = request.GET.get('vip', '')
    marca = request.GET.get('marca', '').lower()
    if buscar:
        productos = [p for p in productos if buscar in p.nombre.lower() or buscar in p.modelo.lower()]
    if vip:
        productos = [p for p in productos if p.vip]
    if marca:
        productos = [p for p in productos if marca in p.marca.nombre.lower()]
    
    return render(request, 'tienda/tienda.html', {'productos': productos})