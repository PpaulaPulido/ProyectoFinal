document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const tipo = urlParams.get('tipo');

    if (tipo) {
        filterByType("/publicacion/tipoRestaurante", tipo, 'resturanteContenedor', 'restaurante');
    }
});

function filterByType(api, tipo, contenedor, nombrePublicacion) {
    fetch(`${api}?tipo=${tipo}`)
        .then(response => response.json())
        .then(data => {
            const contenedorPub = document.getElementById(contenedor);
            if (!contenedorPub) {
                console.error(`No se encontró el contenedor con ID: ${contenedor}`);
                return;
            }

            contenedorPub.innerHTML = '';

            tarjetasPublicacion(data, contenedorPub, nombrePublicacion, 'logo del restaurante', '/res/restauranteDetalleServidorAdmin', {
                id: 'id',
                nombre: 'nombre',
                logo: 'logo',
                tipo: 'tipo',
            });

            // Aquí es donde se asegura que los favoritos se marcan adecuadamente después de cargar las tarjetas.
            // Esperar un momento para asegurarse de que las tarjetas están cargadas antes de marcar los favoritos
            setTimeout(() => {
                fetch('/admin/obtener_favoritosAdmin')
                    .then(response => response.json())
                    .then(data => {
                        data.forEach(fav => {
                            const favIcon = document.querySelector(`.favorite[data-id="${fav.entidad_id}"][data-type="${fav.entidad_tipo}"]`);
                            if (favIcon) {
                                favIcon.style.color = 'red';
                                favIcon.classList.add('active');
                            }
                        });
                    })
                    .catch(error => {
                        console.error('Error al obtener los favoritos:', error);
                    });
            }, 200); 
        })
        .catch(error => {
            console.error('Error al cargar los registros:', error);
        });
}
