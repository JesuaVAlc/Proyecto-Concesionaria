# Proyecto Bimestral de Ingeniería de Software II
# Grupo 7: Celeste Gallardo, Kevin Gómez, Francisco Morales, Jesua Villacis
## Instalación 

1. Clonar el repo
2. Crear un entorno virtual y activarlo
3. Instalar las dependencias del requirements
```bash
    pip install -r requirements.txt
```
4. Aplicar migraciones
```bash
    python manage.py migrate
```
5. Crear un superusuario para poder acceder a acciones de admin en http://127.0.0.1:8000/admin
```bash
    python manage.py createsuperuser
```
6. Iniciar el server
```bash
    python manage.py runserver
```
7. Abrir en el navegador**
```
http://127.0.0.1:8000/usuarios/registro/
```

## Primer Sprint - Creación de usuario y login
- Framework utilizado: Django 
### Distribución de las carpetas
```
Concesionaria/
├── core/                   ← Configuración principal del proyecto
│   ├── settings.py         ← Configuraciones globales del proyecto
│   ├── urls.py             ← Aqui se configuran las URLs que direccionan a los modulos
│   └── wsgi.py
├── apps/                   ← Aplicaciones del sistema = Historias de usuario
│   ├── init.py
│   ├── usuarios/           ← Sprint 1: Registro e inicio de sesión
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── inventario/         ← Sprint 2: Gestión de inventario (pendiente)
│   ├── ventas/             ← Sprint 3: Gestión de ventas (pendiente)
│   └── mantenimiento/      ← Sprint 4: Gestión de mantenimiento (pendiente)
├── templates/              ← Templates de los diferentes modulos o historias de usuario
│   └── dashboard.html
├── manage.py
├── requirements.txt
└── README.md
```


### URLs Disponibles hasta el momento
| URL | Descripción |
|-----|-------------|
| `/users/registro/` | Crear cuenta |
| `/users/login/` | Iniciar sesión |
| `/users/dashboard/` | Panel principal |
| `/admin/` | Panel de administración Django |

## Nota
- Entren al panel de admin con la URL y las credenciales de superusuario para que puedan ver si es que se les creó los usuarios