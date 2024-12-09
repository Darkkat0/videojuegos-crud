# Importaciones necesarias para manejar vistas, formularios, autenticación y mensajes
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import SignupForm, VideojuegoForm  # Formularios personalizados
from .models import Videojuego  # Modelo de Videojuego

def signup_view(request):
    """
    Vista para registrar nuevos usuarios.
    Muestra un formulario de registro y procesa los datos enviados por el usuario.
    Si el formulario es válido, registra al usuario y lo redirige a la página principal.
    """
    if request.method == 'POST':  # Si se envían datos al formulario
        form = SignupForm(request.POST)
        if form.is_valid():  # Valida el formulario
            user = form.save()  # Guarda el usuario en la base de datos
            login(request, user)  # Inicia sesión automáticamente al usuario
            messages.success(request, f"¡Registro exitoso! Bienvenido/a, {user.username}")
            return redirect('home')  # Redirige a la página principal
        else:
            messages.error(request, "Hubo un error con el registro. Por favor, revisa los datos.")
    else:  # Si es una solicitud GET, muestra un formulario vacío
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

@login_required  # Asegura que solo usuarios autenticados puedan acceder
def home(request):
    """
    Vista para mostrar la página principal con la lista de videojuegos.
    Obtiene todos los videojuegos de la base de datos y los pasa al template.
    """
    videojuegos = Videojuego.objects.all()  # Recupera todos los videojuegos
    return render(request, 'home.html', {'videojuegos': videojuegos})

@login_required
def add_videojuego(request):
    """
    Vista para agregar un nuevo videojuego.
    Muestra un formulario para agregar un videojuego y guarda los datos si el formulario es válido.
    """
    if request.method == 'POST':  # Si se envían datos al formulario
        form = VideojuegoForm(request.POST, request.FILES)  # Incluye archivos como imágenes
        if form.is_valid():  # Valida el formulario
            form.save()  # Guarda el nuevo videojuego
            messages.success(request, "Videojuego agregado exitosamente.")
            return redirect('home')  # Redirige a la página principal
    else:  # Si es una solicitud GET, muestra un formulario vacío
        form = VideojuegoForm()
    return render(request, 'add_videojuego.html', {'form': form})

@login_required
def edit_videojuego(request, id):
    """
    Vista para editar un videojuego existente.
    Carga un formulario con los datos del videojuego y los actualiza si el formulario es válido.
    """
    videojuego = get_object_or_404(Videojuego, id=id)  # Obtiene el videojuego por ID o retorna 404 si no existe
    if request.method == 'POST':  # Si se envían datos al formulario
        form = VideojuegoForm(request.POST, request.FILES, instance=videojuego)
        if form.is_valid():  # Valida el formulario
            form.save()  # Guarda los cambios
            messages.success(request, "Videojuego actualizado exitosamente.")
            return redirect('home')  # Redirige a la página principal
    else:  # Si es una solicitud GET, carga el formulario con los datos del videojuego
        form = VideojuegoForm(instance=videojuego)
    return render(request, 'edit_videojuego.html', {'form': form, 'videojuego': videojuego})

@login_required
@csrf_exempt  # Exime esta vista de la protección CSRF
def delete_videojuego(request, id):
    """
    Vista para eliminar un videojuego.
    Elimina un videojuego de la base de datos si la solicitud es POST.
    """
    if request.method == 'POST':  # Verifica que la solicitud sea POST
        videojuego = get_object_or_404(Videojuego, id=id)  # Obtiene el videojuego por ID
        videojuego.delete()  # Elimina el videojuego
        return JsonResponse({'success': True})  # Responde con éxito
    return JsonResponse({'success': False}, status=400)  # Responde con error si no es POST

