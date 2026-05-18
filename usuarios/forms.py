from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput,
    )
    
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo ya está registrado.')
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # Generar username desde el email
        base_username = self.cleaned_data['email'].split('@')[0]
        username = base_username
        counter = 1
        # Si ya existe ese username, agregar número al final
        while Usuario.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1
        user.username = username
        if commit:
            user.save()
        return user
    
class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Correo electrónico o contraseña incorrectos.',
        'inactive': 'Esta cuenta está inactiva.',
    }
    
    username = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)