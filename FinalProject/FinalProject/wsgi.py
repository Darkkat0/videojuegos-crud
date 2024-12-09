import os
# Importa el módulo os para interactuar con las variables de entorno del sistema operativo.

from django.core.wsgi import get_wsgi_application
# Importa la función get_wsgi_application de Django para configurar la aplicación WSGI.

# Establece la configuración predeterminada del proyecto.
# Especifica que el módulo de configuración (settings) que se utilizará es 'FinalProject.settings'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinalProject.settings')

# Obtiene la aplicación WSGI para el proyecto.
# Esta línea expone una instancia de WSGI que será utilizada por servidores compatibles con WSGI,
# como Gunicorn o Apache con mod_wsgi, para servir la aplicación de Django.
application = get_wsgi_application()
