from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroForm, LoginForm

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

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'usuario': request.user})