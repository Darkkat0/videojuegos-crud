# Importaciones necesarias para trabajar con formularios en Django
from django import forms
from django.contrib.auth.models import User  # Modelo predeterminado de usuarios de Django
from django.contrib.auth.forms import UserCreationForm  # Formulario para registrar nuevos usuarios
from .models import Videojuego  # Importación del modelo Videojuego definido en tu aplicación

# Clase para personalizar el formulario de registro de usuarios
class SignupForm(UserCreationForm):
    # Campo adicional para el correo electrónico, que es requerido y se etiqueta como "Correo electrónico"
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        # Define el modelo base para el formulario (en este caso, el modelo User de Django)
        model = User
        # Especifica los campos que aparecerán en el formulario y su orden
        fields = ['username', 'email', 'password1', 'password2']

# Clase para crear un formulario basado en el modelo Videojuego
class VideojuegoForm(forms.ModelForm):
    # Clase interna Meta para configurar el formulario
    class Meta:
        # Define el modelo base para el formulario (en este caso, Videojuego)
        model = Videojuego
        # Especifica los campos del modelo que estarán disponibles en el formulario
        fields = ['nombre', 'descripcion', 'imagen']