function inicializarBuscador() {
    let bars_search = document.getElementById("ctn-bars-search");
    let cover_ctn_search = document.getElementById("cover-ctn-search");
    let inputSearch = document.getElementById("inputSearch");
    let box_search = document.getElementById("box-search");
    let search = document.getElementById('ctn-icon-search');

    if (!box_search) {
        console.error('El elemento ul #box-search no existe en el DOM en el momento de la ejecución del script.');
        return;
    }

    const listaDatos = [
        "Próximos eventos", "Restaurantes", "Emprendimientos",
        "Eventos", 'Tiendas de ropa'
    ];

    listaDatos.forEach(function (item) {
        let liElement = document.createElement("li");
        let aElement = document.createElement("a");

        if (item === 'Restaurantes') {
            aElement.href = "/res/SeccionRestaurante?tipo=res";
        } else if (item === 'Eventos') {
            aElement.href = "/evento/SeccionEvento?tipo=evento";
        } else if (item == 'Emprendimientos') {
            aElement.href = "/emprende/sectionEmprende?tipo=emprende";
        } else if (item == 'Próximos eventos') {
            aElement.href = "/evento/SeccionEvento?tipo=evento";
        } else if (item == "Tiendas de ropa") {
            aElement.href = '/publicacion/emprendimientoTipo?tipo=Tienda%20de%20Ropa'
        }

        aElement.textContent = item;
        let icono = document.createElement("i");
        icono.className = "fas fa-search";
        aElement.prepend(icono);
        liElement.appendChild(aElement);
        box_search.appendChild(liElement);
    });

    document.getElementById("icon-search").addEventListener("click", mostrar_buscador);
    document.getElementById("cover-ctn-search").addEventListener("click", ocultar_buscador);
    inputSearch.addEventListener("keyup", function(event){
        if(event.key === 'Enter'){
            buscarPorTipo();
        }
    });
    search.addEventListener('click',()=>{
        buscarPorTipo();
    })

    
    function mostrar_buscador() {
        bars_search.style.top = "80px";
        cover_ctn_search.style.display = "block";
        inputSearch.focus();

        box_search.innerHTML = '';

        if (inputSearch.value === "") {
            box_search.style.display = "none";
        }
    }

    function ocultar_buscador() {
        bars_search.style.top = "-10px";
        cover_ctn_search.style.display = "none";
        inputSearch.value = "";
        box_search.style.display = "none";
    }

    function buscarPorTipo() {
        const tipo = inputSearch.value.trim().toLowerCase();
        const tipoRestaurantes = {
            'gourmet': 'Gourmet',
            'comida gourmet': 'Gourmet',
            'internacional': 'Comida Internacional',
            'comida internacional': 'Comida Internacional',
            'tematico': 'Restaurante temático',
            'restaurante tematico': 'Restaurante temático',
            'restaurante con vista': 'Restaurante con vista',
            'vista': 'Restaurante con vista',
            'comida rapida': 'Comida rápida',
            'comida chatarra': 'Comida rápida',
            'chatarra': 'Comida rápida',
            'fast food': 'Comida rápida',
            'comida de mar': 'Comida de Mar',
            'de mar': 'Comida de Mar',
            'mar': 'Comida de Mar',
            'mariscos': 'Comida de Mar',
            'frutos del mar': 'Comida de Mar',
            'parrillas y asaderos': 'Parillas y asaderos',
            'parrillas': 'Parillas y asaderos',
            'asaderos': 'Parillas y asaderos',
            'parrillada': 'Parillas y asaderos',
            'barbacoa': 'Parillas y asaderos',
            'grill': 'Parillas y asaderos',
            'bbq': 'Parillas y asaderos'
        };


        const tipoEventos = {
            'danza': 'Evento de danza',
            'evento de danza': 'Evento de danza',
            'baile': 'Evento de danza',
            'eventos de baile': 'Evento de danza',
            'festival de danza': 'Evento de danza',
            'ferias de comida': 'Ferias gastronómicas',
            'ferias gastronomicas': 'Ferias gastronómicas',
            'eventos de comida': 'Ferias gastronómicas',
            'ferias de gastronomia': 'Ferias gastronómicas',
            'feria de comida': 'Ferias gastronómicas',
            'feria gastronómica': 'Ferias gastronómicas',
            'feria tecnologica': 'Ferias tecnológicas',
            'tecnologia': 'Ferias tecnológicas',
            'ferias tecnologicas': 'Ferias tecnológicas',
            'evento tecnológico': 'Ferias tecnológicas',
            'eventos tecnológicos': 'Ferias tecnológicas',
            'exposiciones tecnologicas': 'Ferias tecnológicas',
            'eventos deportivos': 'Eventos deportivos',
            'deportivos': 'Eventos deportivos',
            'deportes': 'Eventos deportivos',
            'deporte': 'Eventos deportivos',
            'competiciones deportivas': 'Eventos deportivos',
            'torneos deportivos': 'Eventos deportivos',
            'exposiciones de arte': 'Exposiciones de arte',
            'exposiciones': 'Exposiciones de arte',
            'muestras de arte': 'Exposiciones de arte',
            'exposiciones artisticas': 'Exposiciones de arte',
            'eventos de teatro': 'Eventos de teatro',
            'teatro': 'Eventos de teatro',
            'obras de teatro': 'Eventos de teatro',
            'funciones de teatro': 'Eventos de teatro',
            'musica': 'Conciertos de música',
            'conciertos de musica': 'Conciertos de música',
            'conciertos': 'Conciertos de música',
            'recitales de música': 'Conciertos de música',
            'eventos musicales': 'Conciertos de música',
            'festival de musica': 'Conciertos de música',
            'ferias de libros': 'Ferias de libros',
            'libros': 'Ferias de libros',
            'feria del libro': 'Ferias de libros',
            'eventos de libros': 'Ferias de libros',
            'feria literaria': 'Ferias de libros'
        };


        const tipoEmprendimientos = {
            'tienda de ropa': 'Tienda de Ropa',
            'tiendas de ropa': 'Tienda de Ropa',
            'ropa': 'Tienda de Ropa',
            'boutique de ropa': 'Tienda de Ropa',
            'moda': 'Tienda de Ropa',
            'vestimenta': 'Tienda de Ropa',
            'artesanias': 'Artesanias',
            'artesanía': 'Artesanias',
            'productos artesanales': 'Artesanias',
            'manualidades': 'Artesanias',
            'emprendimientos de arte': 'Emprendimientos de Arte',
            'pintura': 'Emprendimientos de Arte',
            'arte': 'Emprendimientos de Arte',
            'galería de arte': 'Emprendimientos de Arte',
            'escultura': 'Emprendimientos de Arte',
            'dibujo': 'Emprendimientos de Arte',
            'emprendimientos de mascotas': 'Emprendimiento de Mascotas',
            'mascotas': 'Emprendimiento de Mascotas',
            'animales': 'Emprendimiento de Mascotas',
            'tienda de mascotas': 'Emprendimiento de Mascotas',
            'accesorios para mascotas': 'Emprendimiento de Mascotas',
            'servicios para mascotas': 'Emprendimiento de Mascotas',
            'emprendimientos de comida': 'Emprendimiento Gastronómico',
            'emprendimiento gastronomico': 'Emprendimiento Gastronómico',
            'comida': 'Emprendimiento Gastronómico',
            'gastronomía': 'Emprendimiento Gastronómico',
            'food truck': 'Emprendimiento Gastronómico',
            'restaurante': 'Emprendimiento Gastronómico',
            'cafetería': 'Emprendimiento Gastronómico',
            'pastelería': 'Emprendimiento Gastronómico',
            'panadería': 'Emprendimiento Gastronómico',
            'cafeteria': 'Emprendimiento Gastronómico',
            'pasteleria': 'Emprendimiento Gastronómico',
            'panaderia': 'Emprendimiento Gastronómico',
        };


        const tipoRestaurante = tipoRestaurantes[tipo];
        const tipoEvento = tipoEventos[tipo];
        const tipoEmprendimiento = tipoEmprendimientos[tipo];

        if (tipoRestaurante) {
            buscarRestaurantes(tipoRestaurante);
        } else if (tipoEvento) {
            buscarEventos(tipoEvento);
        } else if (tipoEmprendimiento) {
            buscarEmprendimientos(tipoEmprendimiento);
        } else {
            Swal.fire({
                title: "No se encontraron resultados para tu búsqueda",
                showClass: {
                  popup: `
                    animate__animated
                    animate__fadeInUp
                    animate__faster
                  `
                },
                hideClass: {
                  popup: `
                    animate__animated
                    animate__fadeOutDown
                    animate__faster
                  `
                },customClass: {
                    confirmButton: 'btn-red',
                    popup: 'border-blue',
                    title: 'title-swal',
                    icon: 'icon-swal',
                    container: 'custom-container'
                  }
              });
            
        }

    }

    document.getElementById("inputSearch").addEventListener("keyup", buscador_interno);

    function buscador_interno() {
        let filter = inputSearch.value.toUpperCase();
        let li = box_search.getElementsByTagName("li");

        for (let i = 0; i < li.length; i++) {
            let a = li[i].getElementsByTagName("a")[0];
            let textValue = a.textContent || a.innerText;

            if (textValue.toUpperCase().indexOf(filter) > -1) {
                li[i].style.display = "";
                box_search.style.display = "block";
            } else {
                li[i].style.display = "none";
            }

            if (inputSearch.value === "") {
                box_search.style.display = "none";
            }
        }
    }
}

function buscarRestaurantes(tipo) {
    fetch(`/publicacion/buscar_restaurante?tipo=${tipo}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Respuesta no fue correcta');
            }
            return response.json();
        })
        .then(data => {
            // Manejar los datos de los restaurantes recibidos
            console.log(`Restaurantes de tipo  ${tipo}:`, data);
            window.location.href = `/publicacion/restauranteTipo?tipo=${tipo}`
        })
        .catch(error => {
            console.error('Error al buscar restaurantes:', error);
        });
}

function buscarEventos(tipo) {
    fetch(`/publicacion/buscar_evento?tipo=${tipo}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Respuesta no fue correcta');
            }
            return response.json();
        })
        .then(data => {
            console.log(`Eventos de tipo  ${tipo}:`, data);
            window.location.href = `/publicacion/eventoTipo?tipo=${tipo}`
        })
        .catch(error => {
            console.error('Error al buscar eventos:', error);
        });
}

function buscarEmprendimientos(tipo) {
    fetch(`/publicacion/buscar_emprendimiento?tipo=${tipo}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Respuesta no fue correcta');
            }
            return response.json();
        })
        .then(data => {
            console.log(`Eventos de tipo  ${tipo}:`, data);
            window.location.href = `/publicacion/emprendimientoTipo?tipo=${tipo}`
        })
        .catch(error => {
            console.error('Error al buscar emprendimientos:', error);
        });
}