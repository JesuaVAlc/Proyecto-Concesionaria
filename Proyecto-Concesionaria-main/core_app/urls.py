from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('eliminar/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('estado/<int:user_id>/', views.toggle_estado_usuario, name='toggle_estado_usuario'),
]