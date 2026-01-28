from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy 
from .forms import * 
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Count, Max, Min, Avg
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
                messages.error(request, 'No hay Stock')
            else:
                total = unidades * producto.precio
                if request.user.saldo <= total :
                    messages.error(request, 'No hay saldo suficiente')
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
                    request.user.saldo -= total
                    request.user.save()
                    messages.success(request, 'Compra Realizada')
                    
                return redirect('tienda') 
    else:
        form = CompraForm()
    return render(request, 'tienda/checkout.html', {'producto': producto, 'form': form})


# class CheckoutCreateView(CreateView):
#     model = Compra
#     form_class = CompraForm
#     template_name = 'tienda/checkout.html'
#     success_url = reverse_lazy('tienda')
    
#     def dispatch(self, request, *args, **kwargs):
#         self.producto = get_object_or_404(Producto, pk=kwargs['producto_id'])
#         return super().dispatch(request, *args, **kwargs)
    
#     def form_valid(self, form):
#         unidades = form.cleaned_data['unidades']
#         if unidades > self.producto.unidades:
#             form.add_error('unidades', 'No hay suficientes unidades disponibles.')
#             return self.form_invalid(form) 
#         form.instance.usuario = self.request.user
#         form.instance.producto = self.producto
#         form.instance.importe = unidades * self.producto.precio
#         self.producto.unidades -= unidades
#         self.producto.save()
#         return super().form_valid(form)
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['producto'] = self.producto
#         return context

# class Checkout(LoginRequiredMixin, View):
#     def get(self, request, pk):
#         producto = get_object_or_404(Producto, pk=pk)
#         unidades = int(request.GET.get('unidades', 1))
#         total = unidades * producto.precio
#         return render(request, 'tienda/checkout.html', {'producto': producto, 'unidades': unidades, 'total': total})
#     def post(self, request, pk):
#         producto = get_object_or_404(Producto, pk=pk)
#         unidades = int(request.POST.get('unidades'))
#         usuario = request.user
#         total = unidades * producto.precio
#         if usuario.saldo >= total and unidades <= producto.unidades:
#             Compra.objects.create(usuario=usuario, producto=producto, unidades=unidades, importe=total)
#             usuario.saldo -= total
#             usuario.save()
#             producto.unidades -= unidades
#             producto.save()
#             messages.success(request, "Compra realizada")
#         else:
#             messages.error(request, "No hay suficiente saldo o unidades")
#         return redirect('compra_listado')
    

class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = "tienda/perfil.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        compras = Compra.objects.filter(usuario=self.request.user)
        context['compras'] = compras
        total_gastado = sum(compra.importe for compra in compras)
        context['total_gastado'] = total_gastado

        return context

def informes(request):
    topclientes = Usuario.objects.annotate(total_gastado = Sum("compras__importe")).order_by('total_gastado')[:10]
    top_compras = Usuario.objects.annotate(total_compras=Count("compras")).order_by('-total_compras')[:10]
    estadistica_compra = Compra.objects.aggregate(total_compras = Count('id'), total_importe = Sum('importe'), maximo_importe = Max('importe'), min_importe = Min('importe'), media_importe = Avg('importe')) 
    contexto = {'topclientes': topclientes , 'top_compras': top_compras, 'estadistica_compra':estadistica_compra}
    return render(request, 'tienda/informes.html', contexto)