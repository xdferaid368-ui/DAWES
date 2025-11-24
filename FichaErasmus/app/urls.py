from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('ficha/<int:id>/', views.detalle_alumno, name='detalle_alumno'),
    path('ficha/crear/', views.crear_ficha, name='crear_ficha'),
    path('ficha/<int:pk>/eliminar/', views.eliminar_ficha, name='eliminar_ficha'),
    path('ficha/<int:pk>/editar/', views.editar_ficha, name='editar_ficha'),
]