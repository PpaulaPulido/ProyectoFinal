document.addEventListener('DOMContentLoaded', function () {
    // Obtener el parámetro 'id' de la URL
    const urlParams = new URLSearchParams(window.location.search);
    const idParam = urlParams.get('id');

    Categoria(window.datosEmpredimientos, idParam);
    Categoria(window.empredimientosArtesania, idParam);
    slider_tarjetas();
    generarDatos();
});

function generarDatos() {
    // Obtiene el ID del evento desde la URL
    const urlParams = new URLSearchParams(window.location.search);
    const restaId = parseInt(urlParams.get('id')); // Convierte el ID a un número entero

    function obtenerDatos(typeEmprended, id) {

        // Busca el evento correspondiente en window.datosEventos por su ID
        const negocio = typeEmprended.find(negocio => negocio.id === id);

        // Verifica si se encontró el evento correspondiente
        if (negocio) {

            document.getElementById('title').textContent = negocio.titulo;
            document.querySelector('#negocio').textContent = negocio.negocio;
            document.querySelector('#horario').textContent = negocio.horario;
            document.querySelector('#contacto').textContent = negocio.contacto;
            document.querySelector('#correo').textContent = negocio.correo;


            sitio_web = document.querySelector('#web');
            sitio_web.href = negocio.pagina;
            sitio_web.target = '_blank';

            enlace = document.querySelector('#red1');

            if (negocio.redes[0] !== "") {
                enlace.href = negocio.redes[0];
                enlace.target = "_blank";
            } else {
                enlace.style.display = 'none';
            }

            enlace2 = document.querySelector('#red2');

            if (negocio.redes[1] !== "") {
                enlace2.href = negocio.redes[1];
                enlace2.target = "_blank";
            } else {
                enlace2.style.display = 'none';
            }

            const location_lista = document.getElementById("location");
            negocio.ubicacion.forEach(ubicacion => {
                const nuevaLi = document.createElement("li");
                nuevaLi.textContent = ubicacion;
                location_lista.appendChild(nuevaLi);
            });

        }
    }
    obtenerDatos(window.datosEmpredimientos, restaId);
    obtenerDatos(window.empredimientosArtesania, restaId);

}

function popup_emprendimientos() {
    const urlParams = new URLSearchParams(window.location.search);
    const restaId = parseInt(urlParams.get('id'));
    popupEmprendimientos(restaId);
}

function popupEmprendimientos(idEmpren) {
    let emprendimientos;

    if (idEmpren >= 1 && idEmpren <= window.datosEmpredimientos.length) {
        emprendimientos = window.datosEmpredimientos.find(emprendimiento => emprendimiento.id === idEmpren);
    } else if (idEmpren > window.datosEmpredimientos.length && idEmpren <= window.datosEmpredimientos.length + window.empredimientosArtesania.length) {
        const emprenIndex = idEmpren - window.datosEmpredimientos.length - 1;
        emprendimientos = window.empredimientosArtesania[emprenIndex];
    } else {
        console.error('ID de emprendimiento no encontrado');
        return; // Termina la ejecución si el ID de emprendimiento no es válido
    }

    Swal.fire({
        title: `<span class="custom-title">${emprendimientos.titulo}</span>`,
        html: `
              <div class="div-swal">
              <img src="${emprendimientos.imagen}" alt="imagen emprendimiento" class="imagenEmprendimiento"/>
              <p class="text_swal">${emprendimientos.descripcion}</p>
              <button class="btn_productos"><a href="${emprendimientos.productos}" target="_blank">Ver Productos</a></button>
              </div>
            `,
        customClass: {
            confirmButton: 'btn-red',
            popup: 'border-blue', // Clase CSS para el borde del SweetAlert
            title: 'title-swal',
            icon: 'icon-swal',
            container: 'custom-container'
        }
    });
}
