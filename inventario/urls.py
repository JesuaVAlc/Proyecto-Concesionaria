from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_vehiculos, name='lista_vehiculos'),
    path('crear/', views.crear_vehiculo, name='crear_vehiculo'),
    path('actualizar/<int:pk>/', views.actualizar_vehiculo, name='actualizar_vehiculo'),
    path('eliminar/<int:pk>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('detalle/<int:pk>/', views.detalle_vehiculo, name='detalle_vehiculo'),
]
