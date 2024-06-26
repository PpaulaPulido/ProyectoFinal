document.addEventListener('DOMContentLoaded', function () {

    // Obtener el parámetro 'id' de la URL
    const urlParams = new URLSearchParams(window.location.search);
    const idParam = urlParams.get('id');


    Categoria(window.datosEventos, idParam);
    Categoria(window.eventosTecnologicos, idParam);

    generarBubles();
    slider_tarjetas();
    generarDatos();

});

function generarDatos() {
    const urlParams = new URLSearchParams(window.location.search);
    const eventId = parseInt(urlParams.get('id'));

    function obtenerDatos(typeEvento, id) {
        const evento = typeEvento.find(evento => evento.id === id);

        if (evento) {
            document.getElementById('title').textContent = evento.titulo;
            document.querySelector('#fecha').textContent = evento.fecha;
            document.querySelector('#horario').textContent = evento.horario;
            document.querySelector('#nombres').textContent = evento.organizadores;
            document.querySelector('#contacto').textContent = evento.contacto;

            const sitioWeb = document.querySelector('#web');
            sitioWeb.href = evento.pagina;
            sitioWeb.target = '_blank';

            const enlace = document.querySelector('#red1');
            if (evento.redes[0] !== "") {
                enlace.href = evento.redes[0];
                enlace.target = "_blank";
            } else {
                enlace.style.display = 'none';
            }

            const enlace2 = document.querySelector('#red2');
            if (evento.redes[1] !== "") {
                enlace2.href = evento.redes[1];
                enlace2.target = "_blank";
            } else {
                enlace2.style.display = 'none';
            }

            const locationLista = document.getElementById("location");
            evento.ubicacion.forEach(ubicacion => {
                const nuevaLi = document.createElement("li");
                nuevaLi.textContent = ubicacion;
                locationLista.appendChild(nuevaLi);
            });
        } 
    }
    obtenerDatos(window.datosEventos, eventId);
    obtenerDatos(window.eventosTecnologicos, eventId);
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
    const eventId = parseInt(urlParams.get('id'));

    popupDescripcion(eventId);
}
function popupDescripcion(eventId){

    let evento;

    // Verifica si el ID pertenece a window.datosEventos
    if (eventId >= 1 && eventId <= window.datosEventos.length) {
        evento = window.datosEventos.find(evento => evento.id === eventId);
    }
    // Si no, verifica si pertenece a window.eventosTecnologicos
    else if (eventId >= (window.datosEventos.length + 1) && eventId <= (window.datosEventos.length + window.eventosTecnologicos.length)) {
        const eventoIndex = eventId - window.datosEventos.length;
        evento = window.eventosTecnologicos[eventoIndex - 1];
    }
    // Si el ID no corresponde a ninguno, muestra un mensaje de error
    else {
        console.error("ID de evento no válido");
        return;
    }

    Swal.fire({
        title: `<span class="custom-title">${evento.titulo}</span>`,
        html: `
          <div class = "div-swal">
          <img src="${evento.imagen}" alt="imagen evento" class="imagenRestaurante"/>
          <p class="text_swal">${evento.descripcion}</p>
          </div>
        `,
        customClass: {
            confirmButton: 'btn-red',
            popup: 'border-blue',// Clase CSS para el borde del SweetAlert
            titlle: 'title-swal',
            icon: 'icon-swal',
            container: 'custom-container'
        }
    });
}
function popup_information() {
    const urlParams = new URLSearchParams(window.location.search);
    const eventId = parseInt(urlParams.get('id'));

    // Llama a la función popupInformation con el ID obtenido
    popupInformation(eventId);
}

function popupInformation(eventId) {
    
    let evento;

    // Verifica si el ID pertenece a window.datosEventos
    if (eventId >= 1 && eventId <= window.datosEventos.length) {
        evento = window.datosEventos.find(evento => evento.id === eventId);
    }
    // Si no, verifica si pertenece a window.eventosTecnologicos
    else if (eventId >= (window.datosEventos.length + 1) && eventId <= (window.datosEventos.length + window.eventosTecnologicos.length)) {
        const eventoIndex = eventId - window.datosEventos.length;
        evento = window.eventosTecnologicos[eventoIndex - 1];
    }
    // Si el ID no corresponde a ninguno, muestra un mensaje de error
    else {
        console.error("ID de evento no válido");
        return;
    }

    // Genera el HTML para el evento encontrado
    let eventoHTML = '<h3>Información adicional</h3>';
    eventoHTML += '<ul class="popup_list">';
    evento.informacion_adicional.forEach(information => {
        eventoHTML += `<li class="item_list">${information}</li>`;
    });
    eventoHTML += '</ul>';
    eventoHTML += '<h3 class="popup_title">Consulta tus entradas</h3>';

    if (evento.boletas.length >= 1) {
        eventoHTML += `<button class="btn_boletas"><a href="${evento.boletas}" target="_blank">Clic Aquí</a></button>`;
    } else {
        eventoHTML += `<button class="btn_boletas btn_boletasAG"><a href="#">Agotados</a></button>`;
    }

    // Muestra el popup con la información del evento
    Swal.fire({
        title: `<span class="custom-title">${evento.titulo}</span>`,
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
