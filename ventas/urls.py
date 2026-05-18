from django.urls import path
from . import views

urlpatterns = [
    path('nueva/', views.crear_venta, name='crear_venta'),
    path('comprobante/<int:pk>/', views.comprobante_venta, name='comprobante_venta'),
    path('historial/', views.historial_ventas, name='historial_ventas'), 
]