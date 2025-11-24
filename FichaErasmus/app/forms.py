from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = [
            'apellidos', 'nombre', 'clase', 'sexo', 'fecha_nacimiento',
            'numero_pasaporte', 'direccion', 'numero_telefono', 'numero_movil',
            'email_alumno', 'email_padres', 'profesion_padre', 'profesion_madre',
            'edad_hermanos', 'edad_hermanas', 'mascotas_tener', 'tipo_mascota',
            'problemas_salud', 'es_vegetariano', 'pref_intercambio',
            'puede_alojar', 'larga_duracion', 'firma_alumno', 'firma_padres'
        ]

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'sexo': forms.Select(choices=[
                ('Hombre', 'Hombre'),
                ('Mujer', 'Mujer'),
                ('Otro', 'Otro')
            ]),
            'pref_intercambio': forms.Select(choices=[
                ('chico', 'Un chico'),
                ('chica', 'Una chica'),
                ('da igual', 'Da igual')
            ]),
            'mascotas_tener': forms.CheckboxInput(),
            'es_vegetariano': forms.CheckboxInput(),
            'puede_alojar': forms.CheckboxInput(),
            'larga_duracion': forms.CheckboxInput(),
        }

        labels = {
            'apellidos': 'Apellidos',
            'nombre': 'Nombre',
            'clase': 'Clase',
            'sexo': 'Sexo',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'numero_pasaporte': 'Número de pasaporte',
            'direccion': 'Dirección',
            'numero_telefono': 'Número de teléfono',
            'numero_movil': 'Móvil',
            'email_alumno': 'Correo electrónico del alumno',
            'email_padres': 'Correo electrónico de los padres',
            'profesion_padre': 'Profesión del padre',
            'profesion_madre': 'Profesión de la madre',
            'edad_hermanos': 'Edad de los hermanos',
            'edad_hermanas': 'Edad de las hermanas',
            'mascotas_tener': '¿Tienes mascotas?',
            'tipo_mascota': 'Tipo de mascota',
            'problemas_salud': 'Problemas de salud',
            'es_vegetariano': 'Soy vegetariano/a',
            'pref_intercambio': 'Preferencia de intercambio',
            'puede_alojar': 'Puedo alojar a dos alumnos',
            'larga_duracion': 'Participar en larga duración (4º ESO)',
            'firma_alumno': 'Firma del alumno',
            'firma_padres': 'Firma de los padres',
        }