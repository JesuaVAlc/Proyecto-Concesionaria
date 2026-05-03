from django.urls import path
from . import views

urlpatterns = [
    # Tus otras rutas (login, registro, dashboard)...
    path('login/', views.inicio_sesion, name='login'),
    path('registro/', views.registro, name='registro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('eliminar/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('estado/<int:user_id>/', views.toggle_estado_usuario, name='toggle_estado_usuario'),
   
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'), 
]