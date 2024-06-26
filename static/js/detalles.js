document.addEventListener('DOMContentLoaded', function () {
    // Obtener el parámetro 'id' de la URL
    const urlParams = new URLSearchParams(window.location.search);
    const idParam = urlParams.get('id');

    Categoria(window.datosTarjetas, idParam);
    Categoria(window.restaurantesTematicos, idParam);
    Categoria(window.restaurantesVista, idParam);

    slider_tarjetas();
    generarDatos();
    particulas();

});


function generarDatos() {
    // Obtiene el ID del evento desde la URL
    const urlParams = new URLSearchParams(window.location.search);
    const restaId = parseInt(urlParams.get('id')); // Convierte el ID a un número entero

    function obtenerDatos(typeRes, id) {
        // Busca el evento correspondiente en window.datosEventos por su ID
        const type_resta = typeRes.find(type_resta => type_resta.id === id);

        // Verifica si se encontró el evento correspondiente
        if (type_resta) {

            document.getElementById('title').textContent = type_resta.titulo;
            document.querySelector('#horario').textContent = type_resta.horario;
            document.querySelector('#contacto').textContent = type_resta.contacto;
            document.querySelector('#comidas').textContent = type_resta.comida;
            document.querySelector('#correo').textContent = type_resta.correo;

            sitio_web = document.querySelector('#web');
            sitio_web.href = type_resta.pagina;
            sitio_web.target = '_blank';


            enlace = document.querySelector('#red1');

            if (type_resta.redes[0] !== "") {
                enlace.href = type_resta.redes[0];
                enlace.target = "_blank";
            } else {
                enlace.style.display = 'none';
            }


            enlace2 = document.querySelector('#red2');

            if (type_resta.redes[1] !== "") {
                enlace2.href = type_resta.redes[1];
                enlace2.target = "_blank";
            } else {
                enlace2.style.display = 'none';
            }

            const location_lista = document.getElementById("location");
            type_resta.ubicacion.forEach(ubicacion => {
                const nuevaLi = document.createElement("li");
                nuevaLi.textContent = ubicacion;
                location_lista.appendChild(nuevaLi);

            });


        }
    }
    obtenerDatos(window.datosTarjetas,restaId);
    obtenerDatos(window.restaurantesTematicos,restaId);
    obtenerDatos(window.restaurantesVista,restaId);
}

function popup_menu() {
    const urlParams = new URLSearchParams(window.location.search);
    const restaId = parseInt(urlParams.get('id')); // Convierte el ID a un número entero
    popupmenu(restaId);
}

function popupmenu(eventId) {

    let restaurante;

    if (eventId >= 1 && eventId <= window.datosTarjetas.length) {
        restaurante = window.datosTarjetas.find(rest => rest.id === eventId);
    } 
    else if (eventId >= (window.datosTarjetas.length + 1) && eventId <= (window.datosTarjetas.length + window.restaurantesVista.length)) {
        const eventoIndex = eventId - window.datosTarjetas.length - 1; // Corregir el índice
        restaurante = window.restaurantesVista[eventoIndex]; // No es necesario restar 1 aquí
    } 
    else if(eventId >= (window.datosTarjetas.length + window.restaurantesVista.length + 1) && eventId <= (window.datosTarjetas.length + window.restaurantesVista.length + window.restaurantesTematicos.length)){
        const eventoIndex = eventId - window.datosTarjetas.length - window.restaurantesVista.length - 1; // Corregir el índice
        restaurante = window.restaurantesTematicos[eventoIndex]; // No es necesario restar 1 aquí
    }
    else {
        console.error("ID de evento no válido");
        return;
    }
    

    let menuHtml = '<h3>Nuestro Menú</h3>';
    let i = 1;

    if (restaurante.menu.length >= 2) {
        restaurante.menu.forEach(menuItem => {
            menuHtml += `<h4>Conoce el menú ${i}</h4>`;
            menuHtml += `<p class="screen"> 🍽️<a href="${menuItem}" target="_blank">Ver Menú</a></p>`;
            i++;
        });
    } else {
        restaurante.menu.forEach(menuItem => {
            menuHtml += `<p class="screen"> 🍽️<a href="${menuItem}" target="_blank">Ver Menú</a></p>`;
        });
    }

    Swal.fire({
        title: `<span class="custom-title">${restaurante.titulo}</span>`,
        html: `<div class="div-swal">${menuHtml}</div>`,
        icon: 'info',
        confirmButtonText: 'Cerrar',
        customClass: {
            confirmButton: 'btn-red',
            popup: 'border-blue', // Clase CSS para el borde del SweetAlert
            title: 'title-swal',
            icon: 'icon-swal',
            container: 'custom-container'
        }
    });
}



function popup_nosotros() {

    const urlParams = new URLSearchParams(window.location.search);
    const restaId = parseInt(urlParams.get('id'));
    popupNosotros(restaId);
    
}

function popupNosotros(eventId){

    let type_resta;

    if (eventId >= 1 && eventId <= window.datosTarjetas.length) {
        type_resta = window.datosTarjetas.find(rest => rest.id === eventId);
    } 
    else if (eventId >= (window.datosTarjetas.length + 1) && eventId <= (window.datosTarjetas.length + window.restaurantesVista.length)) {
        const eventoIndex = eventId - window.datosTarjetas.length - 1; // Corregir el índice
        type_resta = window.restaurantesVista[eventoIndex]; // No es necesario restar 1 aquí
    } 
    else if(eventId >= (window.datosTarjetas.length + window.restaurantesVista.length + 1) && eventId <= (window.datosTarjetas.length + window.restaurantesVista.length + window.restaurantesTematicos.length)){
        const eventoIndex = eventId - window.datosTarjetas.length - window.restaurantesVista.length - 1; // Corregir el índice
        type_resta = window.restaurantesTematicos[eventoIndex]; // No es necesario restar 1 aquí
    }
    else {
        console.error("ID de evento no válido");
        return;
    }

    Swal.fire({
        title: `<span class="custom-title">${type_resta.titulo}</span>`,
        html: `
              <div class = "div-swal">
              <img src="${type_resta.imagen}" alt="imagen restaurante" class= "imagenRestaurante"/>
              <p class="text_swal">${type_resta.nosotros}</p>
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
function particulas() {

    // Configuración de particles.js
    particlesJS("particles-js", {
        "particles": {
            "number": {
                "value": 80,
                "density": {
                    "enable": true,
                    "value_area": 800
                }
            },
            "color": {
                "value": "#ffffff"
            },
            "shape": {
                "type": "circle",
                "stroke": {
                    "width": 0,
                    "color": "#000000"
                },
                "polygon": {
                    "nb_sides": 5
                },
                "image": {
                    "src": "img/github.svg",
                    "width": 100,
                    "height": 100
                }
            },
            "opacity": {
                "value": 0.5,
                "random": false,
                "anim": {
                    "enable": false,
                    "speed": 1,
                    "opacity_min": 0.1,
                    "sync": false
                }
            },
            "size": {
                "value": 3,
                "random": true,
                "anim": {
                    "enable": false,
                    "speed": 40,
                    "size_min": 0.1,
                    "sync": false
                }
            },
            "line_linked": {
                "enable": true,
                "distance": 150,
                "color": "#ffffff",
                "opacity": 0.4,
                "width": 1
            },
            "move": {
                "enable": true,
                "speed": 6,
                "direction": "none",
                "random": false,
                "straight": false,
                "out_mode": "out",
                "bounce": false,
                "attract": {
                    "enable": false,
                    "rotateX": 600,
                    "rotateY": 1200
                }
            }
        },
        "interactivity": {
            "detect_on": "canvas",
            "events": {
                "onhover": {
                    "enable": true,
                    "mode": "repulse"
                },
                "onclick": {
                    "enable": true,
                    "mode": "push"
                },
                "resize": true
            },
            "modes": {
                "grab": {
                    "distance": 400,
                    "line_linked": {
                        "opacity": 1
                    }
                },
                "bubble": {
                    "distance": 400,
                    "size": 40,
                    "duration": 2,
                    "opacity": 8,
                    "speed": 3
                },
                "repulse": {
                    "distance": 200,
                    "duration": 0.4
                },
                "push": {
                    "particles_nb": 4
                },
                "remove": {
                    "particles_nb": 2
                }
            }
        },
        "retina_detect": true
    });

}

