// scripts.js

$(document).ready(function() {
    // Espera a que el DOM esté completamente cargado antes de ejecutar el script.

    // Maneja el evento de clic en los botones de eliminación de videojuegos.
    $(".delete-btn").click(function() {
        // Obtiene el ID del videojuego desde el atributo "data-id" del botón.
        const id = $(this).data("id");

        // Muestra un cuadro de confirmación para asegurarse de que el usuario desea eliminar el videojuego.
        if (confirm("¿Estás seguro de que deseas eliminar este videojuego?")) {
            // Realiza una solicitud AJAX para eliminar el videojuego.
            $.ajax({
                url: `/delete_videojuego/${id}/`, // URL para la vista de eliminación del videojuego, con el ID incluido.
                method: "POST", // Método HTTP para enviar la solicitud.
                data: {
                    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(), 
                    // Incluye el token CSRF necesario para validar la solicitud en Django.
                },
                success: function(response) {
                    // Si la respuesta indica éxito, recarga la página para reflejar los cambios.
                    if (response.success) {
                        location.reload(); // Recarga la página actual.
                    }
                }
            });
        }
    });
});
