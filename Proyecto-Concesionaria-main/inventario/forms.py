from datetime import datetime
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
        
    def clean_anio(self):
        anio = self.cleaned_data.get('anio')
        anio_actual = datetime.now().year
        if anio < 1900: 
            raise forms.ValidationError('El año no puede ser anterior a 1900.')
        if anio > anio_actual + 1:
            raise forms.ValidationError(f'El año no puede ser mayor a {anio_actual + 1}.')
        return anio

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor a cero.')
        return precio