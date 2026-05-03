from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # Correo electronico único
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    ROL_CHOICES =[
         ('cliente', 'Cliente'),
        ('vendedor', 'Vendedor'),
        ('recepcionista', 'Recepcionista de Taller'),
        ('administrador', 'Administrador'),
    ]
    
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='cliente')
    telefono = models.CharField(max_length=15, blank=True, null=True)
    cedula = models.CharField(max_length=10, blank=True, null=True, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_rol_display()})"

    @property
    def es_administrador(self):
        return self.rol == 'administrador'

    @property
    def es_vendedor(self):
        return self.rol == 'vendedor'

    @property
    def es_recepcionista(self):
        return self.rol == 'recepcionista'


