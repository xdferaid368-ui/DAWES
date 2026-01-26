from django.shortcuts import render, get_object_or_404, redirect
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

def checkout(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    form = CompraForm()
    return render(request, 'tienda/checkout.html', {'producto': producto, 'form': form})


def checkout(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            unidades = form.cleaned_data['unidades']
            if unidades > producto.unidades:
                form.add_error('unidades', 'No hay suficientes unidades disponibles.')
            else:
                importe = unidades * producto.precio
                Compra.objects.create(
                    usuario=request.user,
                    producto=producto,
                    unidades=unidades,
                    importe=importe, 
                )
                producto.unidades -= unidades
                producto.save()
                return redirect('tienda') 
    else:
        form = CompraForm()
    return render(request, 'tienda/checkout.html', {'producto': producto, 'form': form})


class CheckoutCreateView(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'tienda/checkout.html'
    success_url = reverse_lazy('tienda')

    def dispatch(self, request, *args, **kwargs):
        """
        Este método se ejecuta ANTES del get o del post.
        Aquí obtenemos el producto que se va a comprar.
        """
        self.producto = get_object_or_404(Producto, pk=kwargs['producto_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Este método se ejecuta cuando el formulario es válido.
        Aquí hacemos la lógica de la compra.
        """
        unidades = form.cleaned_data['unidades']

        # Comprobamos si hay stock suficiente
        if unidades > self.producto.unidades:
            form.add_error('unidades', 'No hay suficientes unidades disponibles.')
            return self.form_invalid(form)

        # Asignamos los datos que no vienen del formulario
        form.instance.usuario = self.request.user
        form.instance.producto = self.producto
        form.instance.importe = unidades * self.producto.precio

        # Restamos las unidades al producto
        self.producto.unidades -= unidades
        self.producto.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Enviamos el producto a la plantilla
        """
        context = super().get_context_data(**kwargs)
        context['producto'] = self.producto
        return context