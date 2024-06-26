document.addEventListener('DOMContentLoaded', () => {

    const urlParams = new URLSearchParams(window.location.search);
    const tipo = urlParams.get('tipo');
    
    if (tipo) {
        filterByType("/publicacion/tipoEvento", tipo, 'eventoContenedor', 'evento');
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

            tarjetasPublicacion(data, contenedorPub, nombrePublicacion, 'logo del evento', '/evento/eventoDetalleServidorAdmin', {
                id: 'id',
                nombre: 'nombre',
                logo: 'logo',
                tipo: 'tipo',
            });

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

            }, 500);  // Ajustar el tiempo de espera según sea necesario
        })
        .catch(error => {
            console.error('Error al cargar los registros:', error);
        });
}