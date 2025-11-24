from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('ficha/<int:id>/', views.detalle_alumno, name='detalle_alumno'),
    path('ficha/crear/', views.crear_ficha, name='crear_ficha'),

]