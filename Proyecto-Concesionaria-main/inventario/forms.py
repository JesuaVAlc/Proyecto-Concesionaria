from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'chasis', 'anio', 'precio', 'estado', 'imagen']
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'chasis': 'Número de chasis',
            'anio': 'Año',
            'precio': 'Precio',
            'estado': 'Estado',
            'imagen': 'Imagen del vehiculo',
        }