from django.db import models
from usuarios.models import Usuario
from inventario.models import Vehiculo

class Venta(models.Model):
    TIPO_COMPROBANTE = [
        ('boleta', 'Boleta de Venta (Consumidor Final)'),
        ('factura', 'Factura (Con RUC)'),
    ]
    
    # Relaciones
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.PROTECT, verbose_name="Vehículo Vendido")
    vendedor = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='ventas_realizadas')
    cliente = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='compras_realizadas')
    
    # Datos de Facturación / SRI
    tipo_comprobante = models.CharField(max_length=10, choices=TIPO_COMPROBANTE, default='boleta')
    identificacion = models.CharField(max_length=13, help_text="Cédula (10) o RUC (13)")
    nombre_razon_social = models.CharField(max_length=150, verbose_name="Nombre / Razón Social")
    direccion_fiscal = models.CharField(max_length=255, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=15, blank=True, null=True)
    correo_contacto = models.EmailField(blank=True, null=True)
    
    # Totales (Se calculan automáticamente)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2, help_text="IVA 15%")
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    fecha_venta = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return f"Venta {self.id:05d} - {self.vehiculo.marca} {self.vehiculo.modelo}"