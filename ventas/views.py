from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Venta
from inventario.models import Vehiculo
from usuarios.models import Usuario
from decimal import Decimal

@login_required
def crear_venta(request):
    # Solo vendedores o admins pueden acceder
    if not (request.user.rol in ['vendedor', 'administrador'] or request.user.is_superuser):
        return redirect('dashboard')

    if request.method == 'POST':
        vehiculo_id = request.POST.get('vehiculo_id')
        cliente_id = request.POST.get('cliente_id')
        tipo_comprobante = request.POST.get('tipo_comprobante')
        
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        cliente = get_object_or_404(Usuario, id=cliente_id)
        
        # Calcular totales (IVA 15% Ecuador)
        precio_vehiculo = vehiculo.precio
        subtotal = precio_vehiculo / Decimal('1.15') # Extraer subtotal antes de IVA
        iva = precio_vehiculo - subtotal
        total = precio_vehiculo

        venta = Venta.objects.create(
            vehiculo=vehiculo,
            vendedor=request.user,
            cliente=cliente,
            tipo_comprobante=tipo_comprobante,
            identificacion=request.POST.get('identificacion'),
            nombre_razon_social=request.POST.get('nombre_razon_social'),
            direccion_fiscal=request.POST.get('direccion_fiscal', ''),
            telefono_contacto=request.POST.get('telefono_contacto', ''),
            correo_contacto=request.POST.get('correo_contacto', ''),
            subtotal=subtotal,
            iva=iva,
            total=total
        )
        
        # Cambiar estado del vehículo a Vendido
        vehiculo.estado = 'vendido'
        vehiculo.save()
        
        return redirect('comprobante_venta', pk=venta.pk)

    # Para el GET: Enviar datos para llenar el formulario
    vehiculos_disponibles = Vehiculo.objects.filter(estado='disponible')
    clientes = Usuario.objects.filter(rol='cliente')
    
    return render(request, 'ventas/crear_venta.html', {
        'vehiculos': vehiculos_disponibles,
        'clientes': clientes
    })

@login_required
def comprobante_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    return render(request, 'ventas/comprobante.html', {'venta': venta})

@login_required
def historial_ventas(request):
    # Solo vendedores o admins pueden acceder
    if not (request.user.rol in ['vendedor', 'administrador'] or request.user.is_superuser):
        return redirect('dashboard')
    
    # Si es admin, ve todas las ventas. Si es vendedor, ve solo las suyas.
    if request.user.is_superuser or request.user.es_administrador:
        ventas = Venta.objects.all().order_by('-fecha_venta')
    else:
        ventas = Venta.objects.filter(vendedor=request.user).order_by('-fecha_venta')
        
    return render(request, 'ventas/historial.html', {'ventas': ventas})