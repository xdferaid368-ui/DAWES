from django.urls import path
from . import views

urlpatterns = [
    path("listadoProductos/",views.ListadoProductos.as_view(), name = 'listadoProductos'),
    path("producto/<int:pk>/editar/", views.EditarProducto.as_view(), name='producto_editar'),
    path("producto/<int:pk>/eliminar/", views.EliminarProducto.as_view(), name='producto_eliminar'),
    path("producto/nuevo",views.CrearProducto.as_view(), name='producto_crear'),
    path('', views.listado_productos_compra, name='tienda'),
    path('checkout/<int:producto_id>/', views.checkout, name='checkout'),
    path('informes', views.informes, name='informes'),
    path('perfil/', views.PerfilView.as_view(), name='perfil'),
]
