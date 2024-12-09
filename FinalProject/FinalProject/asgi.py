# Importación del módulo os, que permite interactuar con el sistema operativo
import os

# Importación del método get_asgi_application, que configura y devuelve la aplicación ASGI de Django
from django.core.asgi import get_asgi_application

# Configura la variable de entorno 'DJANGO_SETTINGS_MODULE' con el nombre del archivo de configuración de Django
# En este caso, se está configurando para que utilice 'FinalProject.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinalProject.settings')

# Obtiene y asigna la aplicación ASGI, que es necesaria para manejar conexiones asíncronas
# Esta aplicación será utilizada por servidores ASGI como Daphne o Uvicorn
application = get_asgi_application()
