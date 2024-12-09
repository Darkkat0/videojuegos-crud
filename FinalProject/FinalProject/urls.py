# Importación del módulo admin para habilitar la interfaz de administración de Django
from django.contrib import admin
# Importación de vistas de autenticación predefinidas de Django
from django.contrib.auth import views as auth_views
# Importación de la función path para definir rutas en el proyecto
from django.urls import path
# Importación de vistas personalizadas del archivo views.py
from . import views
# Importación de vistas predefinidas para login y logout
from django.contrib.auth.views import LoginView, LogoutView
# Importación de vistas específicas desde views.py para agregar y editar videojuegos
from .views import add_videojuego, edit_videojuego
# Configuración para manejar archivos multimedia en modo DEBUG
from django.conf import settings
from django.conf.urls.static import static

# Lista de patrones de URL para la aplicación
urlpatterns = [
    # Ruta para la interfaz de administración de Django
    path('admin/', admin.site.urls),
    # Ruta para la página de inicio de sesión, con una plantilla personalizada y redirección al home después del login
    path('login/', LoginView.as_view(template_name='login.html', next_page='/home/'), name='login'),
    # Ruta para cerrar sesión utilizando la vista predefinida LogoutView
    path('logout/', LogoutView.as_view(), name='logout'),
    # Ruta para la vista principal (home), que muestra el formulario de registro
    path('', views.signup_view, name='home'),
    # Ruta para la página de registro de usuarios
    path('signup/', views.signup_view, name='signup'),
    # Ruta para la página principal después de iniciar sesión
    path('home/', views.home, name='home'),
    # Ruta para agregar un nuevo videojuego (vista personalizada)
    path('add_videojuego/', add_videojuego, name='add_videojuego'),
    # Ruta para editar un videojuego específico, identificado por su ID
    path('edit_videojuego/<int:id>/', edit_videojuego, name='edit_videojuego'),
    # Ruta para eliminar un videojuego específico, identificado por su ID
    path('delete_videojuego/<int:id>/', views.delete_videojuego, name='delete_videojuego'),
]

# Configuración adicional para servir archivos multimedia en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
