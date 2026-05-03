from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Usuario
from .forms import RegistroForm, LoginForm

@never_cache
def inicio(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')

@never_cache
def registro(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'usuarios/registro.html', {
                'form': form,
                'registro_exitoso': True
            })
        else:
            return render(request, 'usuarios/registro.html', {
                'form': form,
                'registro_fallido': True
            })
    else:
        form = RegistroForm()

    return render(request, 'usuarios/registro.html', {'form': form})

@never_cache
def inicio_sesion(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'usuarios/login.html', {
                'form': form,
                'login_fallido': True
            })
    else:
        form = LoginForm()

    return render(request, 'usuarios/login.html', {'form': form})

@never_cache
def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@never_cache
@login_required
def dashboard(request):
    # Diccionario base con los datos del usuario logueado
    contexto = {'usuario': request.user}
    
    # Si es admin, le mandamos la lista de TODOS los usuarios (excepto él mismo para que no se auto-elimine)
    if request.user.is_superuser or request.user.es_administrador:
        contexto['lista_usuarios'] = Usuario.objects.exclude(id=request.user.id)
        
    return render(request, 'dashboard.html', contexto)

@never_cache
@login_required
def eliminar_usuario(request, user_id):
    # Validamos por seguridad que solo los administradores puedan borrar
    if not (request.user.is_superuser or request.user.es_administrador):
        return redirect('dashboard')
    
    # Solo aceptamos peticiones POST por seguridad (evita que se borren por escribir la URL)
    if request.method == 'POST':
        usuario_a_eliminar = get_object_or_404(Usuario, id=user_id)
        usuario_a_eliminar.delete()
        
    return redirect('dashboard')

@never_cache
@login_required
def toggle_estado_usuario(request, user_id):
    # Validamos que solo los administradores puedan hacer esto
    if not (request.user.is_superuser or request.user.es_administrador):
        return redirect('dashboard')
    
    if request.method == 'POST':
        usuario_a_modificar = get_object_or_404(Usuario, id=user_id)
        
        # Invertimos el estado actual (si es True pasa a False, y viceversa)
        usuario_a_modificar.is_active = not usuario_a_modificar.is_active
        usuario_a_modificar.save()
        
    return redirect('dashboard')