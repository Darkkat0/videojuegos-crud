#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

# Importa los módulos necesarios para trabajar con el sistema y ejecutar comandos
import os
import sys

def main():
    """Run administrative tasks."""
    # Establece la configuración predeterminada para el proyecto Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinalProject.settings')

    try:
        # Importa y ejecuta las tareas administrativas de Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si Django no está instalado o no se encuentra en el entorno adecuado, lanza un error
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Ejecuta el comando Django que se pasa a través de la línea de comandos
    execute_from_command_line(sys.argv)

# Ejecuta la función principal cuando el script se ejecuta directamente
if __name__ == '__main__':
    main()
