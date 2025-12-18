PASOS PARA ABRIR UN PROYECTO EN DJANGO

1. Creamos un entorno virtual y le ponemos de nombre “env”
	python3 -m venv env

2. Entramos dentro de nuestro entorno virtual
source env/bin/activate

3. Creamos un .txt al que llamamos “requirements” donde le añadimos Django==5.2.7

4. Instalamos lo que hemos introducido dentro de “requirements.txt”
	pip install -r requirements.txt 

5. Creamos nuestro proyecto para poder trabajar en el
django-admin startproject nombre_proyecto .

6. Creamos una aplicación dentro de nuestro proyecto
	python manage.py startapp nombre_aplicación

7. Modificamos settings.py del nombre_proyecto 
INSTALLED_APPS = 
[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nombre_aplicación',
]

8. Probamos el proyecto
	python3 manage.py runserver

-------------------------------------------------------------
PASOS PARA CREACIÓN DE VISTAS EN UN PROYECTO EN DJANGO

1. Dentro de la carpeta del nombre_proyecto nos dirigimos a urls.py para incluir las URLs de nombre_aplicación.
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
              path('admin/', admin.site.urls),
              path('', include('nombre_aplicación.urls'))
    ]

2. Creamos un archivo urls.py dentro de la aplicación nombre_aplicación
	from django.urls import path
  from . import views

  urlpatterns = [
          path('', Inicio.as_view(), name='inicio'),
  ]

3. Modificamos el archivo views.py de nombre_aplicación
	from django.views.generic import TemplateView

	class Inicio(TemplateView):
    		template_name = "app/inicio.html"


4. Creamos una carpeta llamada “templates” en nombre_aplicación y dentro de ella otra carpeta con el nombre de nombre_aplicación.
	nombre_aplicación → templates / nombre_aplicación

5. Dentro de estas carpetas, creamos un archivo inicio.html	
	<!DOCTYPE html>
  <html lang="es">
  <head>
      <title>Principal</title>
  </head>
  <body>
      <h1>Esta es mi pagina estática de renderización</h1>
  </body>
  </html>
  
6. Creamos un base.html de donde es estienda todo
  <!DOCTYPE html>
  <html lang="es">
  <head>
      <title>Página base</title>
  </head>
  <body>

      {% block contenido %}
      {% endblock %}
      
  </body>
  </html>

7. Comprobamos que se visualice correctamente
	python3 manage.py runserver

-------------------------------------------------------------
PASOS PARA CREACIÓN DE MODELOS EN UN PROYECTO DJANGO

1. Añadimos en models.py de nombre_aplicación las clases
	from django.db import models

class nombre_Clase(models.Model):
    class CHOICES (models.TextChoices):
        atributo1 = "atributo1"
        atributo2 = "atributo2"
        atributo3 = "atributo3"
    campo1 = models.CharField(max_length=200)
    campo2 = models.IntegerField()
    campo3 = models.BooleanField()
    campo4 = models.DateField()
    campo5 = models.FloatField()
    campo6 = models.CharField(max_length=15, choices=CHOICES.choices, default='')
    campo7 = models.ForeignKey(MODELO, on_delete=models.CASCADE)
    campo8 = models.EmailField()
    campo9 = models.ManyToManyField('MODELO', through='TablaIntermedia')

    def __str__(self):
        return self.titulo
	
2. Dentro de la terminal para que Django prepare los cambios a realizar
	python3 manage.py makemigrations 

3. La primera vez, hay que realizar una migración para reflejar en base de datos la información necesaria de las aplicaciones incluidas
python3 manage.py migrate

4. Configuramos para que se pueda administrar los datos de nombre_Clase en Django, accediendo a admin.py de nombre_aplicación:
	from django.contrib import admin
  from .models import nombre_Clase 

  admin.site.register(nombre_Clase )

5. Creamos un usuario administrador
	python3 manage.py createsuperuser

6. Accedemos dentro de la aplicación
	python3 manage.py runserver

-------------------------------------------------------------
PASOS PARA CREAR EL CRUD

1. Añadimos en views.py de nombre_aplicación las clases para poder hacer los CRUD y además para poder trabajar con los modelos y formularios
  from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
  from .models import *
  from .forms import *

-------------------------------------------------------------
LISTAR

1. Empezamos con el listar, dentro de nuestra views.py de nombre_aplicación
  class ListarMODELO(ListView):
    model = MODELO
    template_name = "app/listar_MODELO.html"
    context_object_name = "MODELOS"

2. Nos dirigimos a las urls.py de nombre_aplicación y creamos la ruta
  from django.urls import path
  from . import views

  urlpatterns = [
   	path('', views.Inicio.as_view(), name='inicio'),
       
    path('listar_MODELO/', views.ListarMODELO.as_view(), name='listar_MODELO'),
  ]

3. Ahora dentro de nuestro templates / nombre_aplicación, creamos un html llamado, listar_MODELO.html donde añadamos
  {% extends 'app/base.html' %}

  {% block contenido %}
      <h1>Lista de MODELO</h1>
      <table>
      <thead>
      <tr>
          <th>CAMPO 1</th>
          <th>CAMPO 2</th>
          <th>CAMPO 3</th>
          <th>ACCIONES</th>
      </tr>
      </thead>
      <tbody>
      {% for MODELO in MODELOS %}
          <tr>
            <td>{{ MODELO.campo1 }}</td>
            <td>{{ MODELO.campo2 }}</td>
            <td>{% if MODELO.campo3%}
                        Sí
                    {% else %}
                        No
                    {% endif %} 
            </td>
            <td>
                <a href="{% url 'detalles_MODELO' MODELO.pk %}">Ver detalles</a>
                <a href="{% url 'actualizar_MODELO' MODELO.pk %}">Editar</a>
                <a href="{% url 'eliminar_MODELO' MODELO.pk %}">Eliminar</a>
            </td>
        </tr>
      {% endfor %}
      </tbody>
      </table>
      {% endblock %}

-------------------------------------------------------------
CREAR

1. Pasamos a crear, dentro de nuestra views.py de nombre_aplicación
  class CrearMODELO(CreateView):
    model = MODELO
    form_class = MODELOForm            
    template_name = "app/crear_MODELO.html"
    success_url = reverse_lazy('listar_MODELO')

2. Nos creamos un forms.py dentro de nuestra nombre_aplicación
  from django import forms
  from .models import *

  class MODELOForm(forms.ModelForm):
      class Meta:
          model = MODELO
          fields = ['campo1', 'campo2', 'campo3']

3. Nos dirigimos a las urls.py de nombre_aplicación y creamos la ruta
  from django.urls import path
  from . import views

  urlpatterns = [
   	path('', views.Inicio.as_view(), name='inicio'),
       
    path('listar_MODELO/', views.ListarMODELO.as_view(), name='listar_MODELO'),
    path('crear_MODELO/', views.CrearMODELO.as_view(), name='crear_MODELO'),
  ]

4. Ahora dentro de nuestro templates / nombre_aplicación, creamos un html llamado, crear_MODELO.html donde añadamos
  {% extends 'app/base.html' %}

  {% block contenido %}
      <h1>Nuevo MODELO</h1>

          <form method="post">
              {% csrf_token %}

              {{ form.non_field_errors }}

              {{ form.as_p }}

              <button type="submit">Guardar</button>
              <a href="{% url 'listar_MODELO' %}">Volver al listado</a>
              <a href="{% url 'inicio' %}">Volver a inicio</a>
          </form>

  {% endblock %}

-------------------------------------------------------------
DETALLES

1. Pasamos a los detalles, dentro de nuestra views.py de nombre_aplicación
  class DetallesMODELO(DetailView):
    model = MODELO          
    template_name = "app/detalles_MODELO.html"
    context_object_name = "MODELO"

2. Nos dirigimos a las urls.py de nombre_aplicación y creamos la ruta
  from django.urls import path
  from . import views

  urlpatterns = [
   	path('', views.Inicio.as_view(), name='inicio'),
       
    path('listar_MODELO/', views.ListarMODELO.as_view(), name='listar_MODELO'),
    path('crear_MODELO/', views.CrearMODELO.as_view(), name='crear_MODELO'),
    path('detalles_MODELO/', views.DetallesMODELO.as_view(), name='detalles_MODELO'),
  ]

3. Ahora dentro de nuestro templates / nombre_aplicación, creamos un html llamado, detalles_MODELO.html donde añadamos
    {% extends 'app/base.html' %}

    {% block contenido %}

        <h1>Detalles del MODELO {{ MODELO.nombre }} </h1>

        <p><strong>Campo1:</strong> {{ MODELO.campo1 }}</p>
        <p><strong>Campo2:</strong> {% if MODELO.campo2 %}Sí{% else %}No{% endif %}</p>
        <p><strong>Campo3:</strong> {{ MODELO.campo3 }}</p>

      <a href="{% url 'listar_MODELOS' %}">Volver al listado</a>
      <a href="{% url 'inicio' %}">Volver a inicio</a>


    {% endblock %}

-------------------------------------------------------------
ACTUALIZAR

1. Pasamos a actualizar, dentro de nuestra views.py de nombre_aplicación
  class ActualizarMODELO(UpdateView):
    model = MODELO          
    form_class = MODELOForm            
    template_name = "app/actualizar_MODELO.html"
    success_url = reverse_lazy('listar_MODELO')

2. Nos dirigimos a las urls.py de nombre_aplicación y creamos la ruta
  from django.urls import path
  from . import views

  urlpatterns = [
   	path('', views.Inicio.as_view(), name='inicio'),
       
    path('listar_MODELO/', views.ListarMODELO.as_view(), name='listar_MODELO'),
    path('crear_MODELO/', views.CrearMODELO.as_view(), name='crear_MODELO'),
    path('detalles_MODELO/', views.DetallesMODELO.as_view(), name='detalles_MODELO'),
    path('actualizar_MODELO/', views.ActualizarMODELO.as_view(), name='actualizar_MODELO'),
  ]

3. Ahora dentro de nuestro templates / nombre_aplicación, creamos un html llamado, actualizar_MODELO.html donde añadamos
  {% extends 'app/base.html' %}

  {% block contenido %}

      <h1>Actualizar MODELO {{MODELO.nombre}}</h1>

      <div>
      <form method="post">
          {% csrf_token %}
          {{ form.as_p }}

          <button type="submit">Guardar</button>

          <a href="{% url 'listar_MODELOS' %}>Volver al listado</a>
          <a href="{% url 'inicio' %}>Volver a inicio</a>
      </form>

  {% endblock %}

-------------------------------------------------------------
BORRAR

1. Pasamos a actualizar, dentro de nuestra views.py de nombre_aplicación
  class EliminarMODELO(DeleteView):
      model = MODELO
      template_name = "app/eliminar_MODELO.html"
      success_url = reverse_lazy('listar_MODELO')    

2. Nos dirigimos a las urls.py de nombre_aplicación y creamos la ruta
  from django.urls import path
  from . import views

  urlpatterns = [
   	path('', views.Inicio.as_view(), name='inicio'),
       
    path('listar_MODELO/', views.ListarMODELO.as_view(), name='listar_MODELO'),
    path('crear_MODELO/', views.CrearMODELO.as_view(), name='crear_MODELO'),
    path('detalles_MODELO/', views.DetallesMODELO.as_view(), name='detalles_MODELO'),
    path('actualizar_MODELO/', views.ActualizarMODELO.as_view(), name='actualizar_MODELO'),
    path('eliminar_MODELO/', views.EliminarMODELO.as_view(), name='eliminar_MODELO'),
  ]

3. Ahora dentro de nuestro templates / nombre_aplicación, creamos un html llamado, eliminar_MODELO.html donde añadamos
  {% extends 'app/base.html' %}

  {% block contenido %}

      <h1>Eliminar cliente</h1>

          <p>¿Seguro que deseas eliminar <strong>{{ MODELO.nombre }}</strong>?</p>

          <form method="post" style="display:inline;">
              {% csrf_token %}
              <button type="submit">Sí, eliminar</button>
          </form>

          <a href="{% url 'listar_MODELO' %}">Cancelar</a>

  {% endblock %}

-------------------------------------------------------------
HACER PÁGINAS ESTÁTICAS EN UN PROYECTO DJANGO

1. Modificamos settings.py del nombre_proyecto 
	STATIC_URL = 'static/'
  STATIC_ROOT = BASE_DIR / 'static'

2. Creamos una nueva carpeta llamada “static” dentro de nuestro nombre_aplicación y dentro de ella creamos la carpeta de “css” y “js”

3. Creamos el css correspondiente y se lo añadimos a nuestro base.html
  {% load static %}
  <!DOCTYPE html>
  <html lang="es">
  <head>
      <link rel="stylesheet" href="{% static 'css/base.css' %}">
  </head>
  <body>

      {% block contenido %}
      {% endblock %}
      
  </body>
  </html>


