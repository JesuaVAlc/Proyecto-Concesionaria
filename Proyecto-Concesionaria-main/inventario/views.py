from urllib import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.
@login_required
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('-fecha_registro')
    if request.user.rol == 'cliente':
        return render(request, 'inventario/galeria.html', {'vehiculos': vehiculos})
    else:
        vehiculos = Vehiculo.objects.all().order_by('-fecha_registro')
        return render(request, 'inventario/lista.html', {'vehiculos': vehiculos})


@login_required
def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'inventario/crear.html', {
                'form': VehiculoForm(),
                'registro_exitoso': True
            })
        else:
            return render(request, 'inventario/crear.html', {
                'form': form,
                'registro_fallido': True
            })
    else:
        form = VehiculoForm()
    return render(request, 'inventario/crear.html', {'form': form})

@login_required
def actualizar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo, files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'inventario/actualizar.html', {
                'form': form,
                'actualizacion_exitosa': True,
                'vehiculo': vehiculo
            })
        else:
            return render(request, 'inventario/actualizar.html', {
                'form': form,
                'actualizacion_fallida': True,
                'vehiculo': vehiculo
            })
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'inventario/actualizar.html', {
        'form': form,
        'vehiculo': vehiculo
    })

@login_required
def eliminar_vehiculo(request, pk):
    if request.method == 'POST':
        vehiculo = get_object_or_404(Vehiculo, pk=pk)
        vehiculo.delete()
    
    return redirect('lista_vehiculos')