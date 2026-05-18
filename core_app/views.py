from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from usuarios.models import Usuario

# Create your views here.
@never_cache
@login_required
def dashboard(request):
    contexto = {'usuario': request.user}
    
    if request.user.is_superuser or request.user.es_administrador:
        contexto['lista_usuarios'] = Usuario.objects.exclude(id=request.user.id)
        
    return render(request, 'dashboard.html', contexto)

@never_cache
@login_required
def eliminar_usuario(request, user_id):
    if not (request.user.is_superuser or request.user.es_administrador):
        return redirect('dashboard')
    
    if request.method == 'POST':
        usuario_a_eliminar = get_object_or_404(Usuario, id=user_id)
        usuario_a_eliminar.delete()
        
    return redirect('dashboard')

@never_cache
@login_required
def toggle_estado_usuario(request, user_id):
    if not (request.user.is_superuser or request.user.es_administrador):
        return redirect('dashboard')
    
    if request.method == 'POST':
        usuario_a_modificar = get_object_or_404(Usuario, id=user_id)
        usuario_a_modificar.is_active = not usuario_a_modificar.is_active
        usuario_a_modificar.save()
        
    return redirect('dashboard')