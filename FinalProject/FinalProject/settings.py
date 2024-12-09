from pathlib import Path  # Importación para trabajar con rutas de archivos de manera eficiente y segura
import os  # Importación para interactuar con el sistema operativo

# Construye rutas dentro del proyecto, por ejemplo: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configuraciones rápidas para desarrollo (no aptas para producción)
# Ver: https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# Advertencia de seguridad: Mantén la clave secreta confidencial en producción
SECRET_KEY = 'django-insecure-*u1vr++7iv6e10fi!wz%1-!^j0)p8hdo!$f553#r-14hug0wnf'

# Advertencia de seguridad: Desactiva DEBUG en producción
DEBUG = True

# Hosts permitidos para el proyecto (vacío por defecto)
ALLOWED_HOSTS = []


# Definición de la aplicación

INSTALLED_APPS = [
    # Aplicaciones integradas de Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Aplicaciones personalizadas del proyecto
    'FinalProject',
]

MIDDLEWARE = [
    # Middleware que gestiona la seguridad y funcionalidades del proyecto
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de las URL raíz del proyecto
ROOT_URLCONF = 'FinalProject.urls'

# Configuración de las plantillas HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Motor de plantillas
        'DIRS': ["FinalProject/templates"],  # Directorios adicionales para buscar plantillas
        'APP_DIRS': True,  # Habilita la búsqueda de plantillas dentro de las aplicaciones instaladas
        'OPTIONS': {
            'context_processors': [  # Procesadores de contexto disponibles en las plantillas
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Aplicación WSGI (para manejar solicitudes en producción)
WSGI_APPLICATION = 'FinalProject.wsgi.application'


# Configuración de la base de datos
# Ver: https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Motor de base de datos
        'NAME': BASE_DIR / 'db.sqlite3',  # Archivo de base de datos
    }
}


# Validación de contraseñas
# Ver: https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Configuración de internacionalización
# Ver: https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'es-mx'  # Idioma del proyecto
TIME_ZONE = 'America/Mexico_City'  # Zona horaria del proyecto
USE_I18N = True  # Habilitar traducción de texto
USE_TZ = True  # Usar zonas horarias


# Archivos estáticos (CSS, JavaScript, Imágenes)
# Ver: https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/static/'  # URL base para archivos estáticos
STATICFILES_DIRS = [BASE_DIR / 'static']  # Directorios donde se almacenan archivos estáticos del proyecto

# Configuración para manejar archivos cargados por el usuario
MEDIA_URL = '/media/'  # URL base para archivos multimedia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Directorio donde se guardan los archivos multimedia

# Configuración de la clave primaria predeterminada
# Ver: https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuraciones de redirección para el sistema de autenticación
LOGIN_REDIRECT_URL = 'home'  # Página a la que se redirige después de iniciar sesión
LOGOUT_REDIRECT_URL = '/signup.html'  # Página a la que se redirige después de cerrar sesión