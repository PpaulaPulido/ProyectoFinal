document.addEventListener('DOMContentLoaded', () => {

    generarDatos();
    calificacion();

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

    fetch(`/emprende/emprendimientoDetalleJson/${id}`)
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
            galeria('publicacion/galeriaImagenes/Emprendimiento');

            if (callback) {
                callback(data);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function mostrarDatos(data) {
    document.getElementById('title').textContent = data.nombreempre;
    document.getElementById('negocio').textContent = data.tipoempre;
    document.getElementById('nombreEmpre').textContent = data.nombreempre;
    document.querySelector('#contacto').textContent = data.telempre;
    document.querySelector('#correo').textContent = data.correoempre || 'No aplica';

    let datoAdminSelector = document.querySelector('#nombreAdmin');
    let datosAdmin = (data.administrador) ? `Publicado por ${data.administrador + data.apellidoAdm}` : '';
    datoAdminSelector.innerHTML = datosAdmin;

    document.querySelector('#horarioText').textContent = data.horarioempre;
    const divhorario = document.getElementById('horario');
    divhorario.classList.add('horario');


    const horaEntradaTexto = document.createElement('p');
    horaEntradaTexto.textContent = `Hora de apertura: ${data.horarioApertura}`;

    const horaSalidaTexto = document.createElement('p');
    horaSalidaTexto.textContent = `Hora de cierre: ${data.horarioCierre}`;

    divhorario.appendChild(horaEntradaTexto);
    divhorario.appendChild(horaSalidaTexto);

    const sitio_web = document.querySelector('#web');
    sitio_web.href = data.paginaempre;
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
    const ubicaciones = data.ubicaciones_emprende ? data.ubicaciones_emprende.split('; ') : [];
    ubicaciones.forEach(ubicacion => {
        const nuevaLi = document.createElement("li");
        nuevaLi.textContent = ubicacion;
        location_lista.appendChild(nuevaLi);
    });
}



function popup_emprendimientos() {
    const urlParams = new URLSearchParams(window.location.search);
    const id = parseInt(urlParams.get('id'));

    fetch(`/emprende/emprendimientoDetalleJson/${id}`)
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
            popupEmprendimientos(data)
            if (callback) {
                callback(data);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function popupEmprendimientos(data) {
    
    Swal.fire({
        title: `<span class="custom-title">${data.nombreempre}</span>`,
        html: `
              <div class="div-swal">
              <img src="${data.logo}" alt="imagen emprendimiento" class="imagenEmprendimiento"/>
              <p class="text_swal">${data.descripempre}</p>
              <button class="btn_productos"><a href="${data.producempre}" target="_blank">Ver Productos</a></button>
              </div>
            `,
        customClass: {
            confirmButton: 'btn-red',
            popup: 'border-blue', 
            title: 'title-swal',
            icon: 'icon-swal',
            container: 'custom-container'
        }
    });
}
