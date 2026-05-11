from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('vendido', 'Vendido'),
        ('reservado', 'Reservado'),
    ]
    
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    chasis = models.CharField(max_length=50, unique=True)
    anio = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='vehiculos/', blank=True, null=True)

    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"
