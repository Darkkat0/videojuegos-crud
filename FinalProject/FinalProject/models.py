# Importación del módulo models, que se utiliza para definir modelos en Django
from django.db import models


# Modelo que representa un videojuego en la base de datos
class Videojuego(models.Model):
    # Campo para almacenar el nombre del videojuego, con un límite de 100 caracteres
    nombre = models.CharField(max_length=100)
    # Campo para almacenar una descripción del videojuego, sin límite de caracteres
    descripcion = models.TextField()
    # Campo opcional para cargar una imagen del videojuego
    # El archivo se almacenará en la carpeta 'videojuegos/' dentro del directorio de medios configurado
    imagen = models.ImageField(upload_to='videojuegos/', null=True, blank=True)

    # Método especial para definir la representación en cadena del modelo
    def __str__(self):
        # Devuelve el nombre del videojuego como su representación en cadena
        return self.nombre