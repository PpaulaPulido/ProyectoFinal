document.addEventListener('DOMContentLoaded', () => {

    generarDatos();
    calificacion();
    generarBubles();
});

function calificacion() {
    const rating = document.getElementById('rating');
    for (let i = 0; i < 5; i++) {
        const star = document.createElement('i');
        star.classList.add("bi", "bi-star-fill", "star");
        rating.appendChild(star);
    }
}
function generarDatos(callback) {
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');

    fetch(`/evento/eventoDetalleJson/${id}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la solicitud');
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                console.error(data.error);
                return;
            }
            console.log(data); // Ver los datos obtenidos en la consola
            mostrarDatos(data);
            galeria('publicacion/galeriaImagenes/evento');

            if (callback) {
                callback(data);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function mostrarDatos(data) {
    document.getElementById('title').textContent = data.nombreeven;
    document.getElementById('fecha').textContent = data.fechas_eventos;
    document.getElementById('nombreEvento').textContent = data.nombreeven;
    document.querySelector('#contacto').textContent = data.contacto;
    document.querySelector('#eventoTipo').textContent = data.tipoevento;
    document.querySelector('#correo').textContent = data.correoeven || 'No aplica';
    let datoAdminSelector = document.querySelector('#nombreAdmin');

    let datosAdmin = (data.administrador) ? `Publicado por ${data.administrador + data.apellidoAdm}` : '';
    datoAdminSelector.innerHTML = datosAdmin;

    const divhorario = document.getElementById('horario');
    divhorario.classList.add('horario');

    const horaEntradaTexto = document.createElement('p');
    horaEntradaTexto.textContent = `Hora de apertura: ${data.hora_entrada}`;

    const horaSalidaTexto = document.createElement('p');
    horaSalidaTexto.textContent = `Hora de cierre: ${data.hora_salida}`;

    divhorario.appendChild(horaEntradaTexto);
    divhorario.appendChild(horaSalidaTexto);

    const sitio_web = document.querySelector('#web');
    sitio_web.href = data.paginaeven;
    sitio_web.target = '_blank';

    const redes = data.redes_sociales ? data.redes_sociales.split('; ') : [];
    const enlace = document.querySelector('#red1');
    if (redes[0]) {
        enlace.href = redes[0].split(': ')[1];
        enlace.target = "_blank";
    } else {
        enlace.style.display = 'none';
    }

    const enlace2 = document.querySelector('#red2');
    if (redes[1]) {
        enlace2.href = redes[1].split(': ')[1];
        enlace2.target = "_blank";
    } else {
        enlace2.style.display = 'none';
    }

    const location_lista = document.getElementById("location");
    const ubicaciones = data.ubicaciones_eventos ? data.ubicaciones_eventos.split('; ') : [];
    ubicaciones.forEach(ubicacion => {
        const nuevaLi = document.createElement("li");
        nuevaLi.textContent = ubicacion;
        location_lista.appendChild(nuevaLi);
    });
}
function generarBubles() {
    // Obtener el contenedor de burbujas
    const bubblesContainer = document.getElementById('bubblesContainer');

    // Números para los estilos
    const numbers = [11, 12, 24, 10, 14, 23, 18, 16, 19, 20, 22, 25, 18, 21, 15, 13, 27, 17, 13, 28, 11, 12, 24, 10, 14, 23, 18, 16, 19, 20, 22, 25, 18, 21, 15, 13, 27, 17, 13, 28, 12, 24, 10, 14, 23, 18, 16, 19, 20, 22, 25, 18, 21, 15, 13, 27, 17, 13, 28];

    // Generar los span dinámicamente
    numbers.forEach(number => {
        const span = document.createElement('span');
        span.style.setProperty('--i', number);
        bubblesContainer.appendChild(span);
    });

}
function popup_descripcion() {
    const urlParams = new URLSearchParams(window.location.search);
    const id = parseInt(urlParams.get('id'));

    fetch(`/evento/eventoDetalleJson/${id}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la solicitud');
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                console.error(data.error);
                return;
            }
            popupDescripcion(data)

            if (callback) {
                callback(data);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
  
}
function popupDescripcion(data){

    Swal.fire({
        title: `<span class="custom-title">${data.nombreeven}</span>`,
        html: `
          <div class = "div-swal">
          <img src="${data.logo}" alt="imagen evento" class="imagenPublicacion"/>
          <p class="text_swal">${data.descripeven}</p>
          </div>
        `,
        customClass: {
            confirmButton: 'btn-red',
            popup: 'border-blue',
            titlle: 'title-swal',
            icon: 'icon-swal',
            container: 'custom-container'
        }
    });
}

function popup_information() {
    const urlParams = new URLSearchParams(window.location.search);
    const id = parseInt(urlParams.get('id'));

    fetch(`/evento/eventoDetalleJson/${id}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la solicitud');
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                console.error(data.error);
                return;
            }
            popupInformation(data)

            if (callback) {
                callback(data);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function popupInformation(data) {
    
    // Genera el HTML para el evento encontrado
    let eventoHTML = '<h3>Información adicional</h3>';
    eventoHTML += '<div class="popup_infoAdicional">';
    eventoHTML += `<p class="infoAdicional">${data.infoAdicional}</p>`
    eventoHTML += '</div>';
    eventoHTML += '<h3 class="popup_title">Consulta tus entradas</h3>';

    if (data.boletaseven.length >= 1) {
        eventoHTML += `<button class="btn_boletas"><a href="${data.boletaseven}" target="_blank">Clic Aquí</a></button>`;
    } else {
        eventoHTML += `<button class="btn_boletas btn_boletasAG"><a href="#">Agotados</a></button>`;
    }

    // Muestra el popup con la información del evento
    Swal.fire({
        title: `<span class="custom-title">${data.nombreeven}</span>`,
        html: `<div class="div-swal">${eventoHTML}</div>`,
        icon: 'info',
        confirmButtonText: 'Cerrar',
        customClass: {
            confirmButton: 'btn-red',
            popup: 'border-blue',
            title: 'title-swal',
            icon: 'icon-swal',
            container: 'custom-container'
        }
    });
}
