from django import forms
from .models import *

class ProductoEditarForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','modelo','unidades','precio','vip','marca' ]

class CheckoutForm(forms.Form):
    unidades = forms.IntegerField(min_value=1, label= 'unidades')
    promocion = forms.IntegerField(required = False )
    