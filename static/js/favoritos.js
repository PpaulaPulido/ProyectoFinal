document.addEventListener('DOMContentLoaded', function () {

    listaFavoritosServidor();

    // Agregar event listener para capturar clics en favoritos
    document.addEventListener('click', function (event) {
        if (event.target.classList.contains('favorite')) {
            const eventId = event.target.getAttribute('data-event-id');
            getFavorite(eventId);
        }
    });


});
function container_fav() {

    // Obtener los eventos favoritos del localStorage
    const favoritos = JSON.parse(localStorage.getItem('favoritos')) || [];
    const favoritosRes = JSON.parse(localStorage.getItem('favoritosRes')) || [];
    const favoritosEm = JSON.parse(localStorage.getItem('favoritosEm')) || [];

    if (favoritos.length === 0 && favoritosRes.length === 0 && favoritosEm.length === 0) {
        let camposVacios = true;
        return camposVacios;

    } else {
        renderFavorite(favoritos, window.datosEventos,'evento');
        renderFavorite(favoritos, window.eventosTecnologicos,'evento');
        renderFavorite(favoritosRes, window.datosTarjetas,'res');
        renderFavorite(favoritosRes, window.restaurantesTematicos,'res');
        renderFavorite(favoritosRes, window.restaurantesVista,'res');
        renderFavorite(favoritosEm, window.datosEmpredimientos,'emprende');
        renderFavorite(favoritosEm, window.empredimientosArtesania,'emprende');
        return false;
    }
}
function renderFavorite(lista, type,tipo) {

    const detalleResUrl = 'http://127.0.0.1:3036/res/restauranteDetalle';
    const detalleEventoUrl = 'http://127.0.0.1:3036/evento/eventoDetalle';
    const detalleEmprendeUrl = 'http://127.0.0.1:3036/emprende/emprendeDetalle';
    // Iterar sobre los eventos favoritos y mostrarlos en la interfaz de usuario
    lista.forEach(function (eventoId) {

        const idNumero = parseInt(eventoId);
        const evento = type.find(e => e.id === idNumero);
        console.log(evento);
        if (evento) {
            // Crear elementos HTML para mostrar la información del evento
            const container_fav = document.querySelector('#favoritos');

            const divTarjeta = document.createElement('div');
            divTarjeta.classList.add('container_tarjeta');
        
            const favorite = document.createElement('i');
            favorite.classList.add("bi", "bi-heart-fill", "favorite");
            favorite.setAttribute('data-event-id', evento.id);

            const cardFavorite = document.createElement('div');
            cardFavorite.classList.add('tipo_imagen_container');
        
            const content_img = document.createElement('div');
            content_img.classList.add('tipo_imagen');

            let imgFavorito = document.createElement('img');
            imgFavorito.src = evento.galeria[3];
            imgFavorito.alt = `Imagen de ${evento.titulo}`;

            const divContenido = document.createElement('div');
            divContenido.classList.add('contenido_texto');
        
            const titulo = document.createElement('p');
            titulo.textContent = evento.titulo;

            const divContainer = document.createElement('div');
            divContainer.classList.add('container');
        
            const rating = document.createElement('div');
            rating.classList.add("rating2");

            for (let i = 0; i < 5; i++) {
                const estrella = document.createElement('input');
                estrella.type = 'radio';
                estrella.name = `rating${evento.id}`;
                estrella.setAttribute('style', '--c: #ff9933');
                rating.appendChild(estrella);
            }

            const divBoton = document.createElement('div');
            divBoton.classList.add('container_btn');

            let enlace = document.createElement('a');

            if (tipo === 'res') {
                enlace.href = `${detalleResUrl}?id=${evento.id}&tipo=res`;
            } else if (tipo === 'evento') {
                enlace.href = `${detalleEventoUrl}?id=${evento.id}&tipo=evento`;
            } else {
                enlace.href = `${detalleEmprendeUrl}?id=${evento.id}&tipo=emprende`;
            }
            
            const boton = document.createElement('button');
            boton.classList.add('btn');
        
            const span1 = document.createElement('span');
            span1.classList.add('btn-text-one');
            span1.textContent = "te interesa";
        
            const span2 = document.createElement('span');
            span2.classList.add('btn-text-two');
            span2.textContent = "mira más!";

            boton.appendChild(span1);
            boton.appendChild(span2);
            enlace.appendChild(boton);
            divBoton.appendChild(enlace);
        
            divContainer.appendChild(rating);
        
            divContenido.appendChild(titulo);
            divContenido.appendChild(divContainer);
            divContenido.appendChild(divBoton);
        
            content_img.appendChild(imgFavorito);
            cardFavorite.appendChild(content_img);
            cardFavorite.appendChild(favorite);
            divTarjeta.appendChild(cardFavorite);
            divTarjeta.appendChild(divContenido);
            container_fav.appendChild(divTarjeta);

        }
    });
}

function getFavorite(eventId) {
    // Obtener los eventos favoritos del localStorage
    let favoritos = JSON.parse(localStorage.getItem('favoritos')) || [];
    let favoritosRes = JSON.parse(localStorage.getItem('favoritosRes')) || [];
    let favoritosEm = JSON.parse(localStorage.getItem('favoritosEm')) || [];

    // Verificar si el evento está en alguna de las listas
    const indexFavoritos = favoritos.indexOf(eventId);
    const indexFavoritosRes = favoritosRes.indexOf(eventId);
    const indexFavoritosEm = favoritosEm.indexOf(eventId);


    // Eliminar el evento de la lista correspondiente
    if (indexFavoritos !== -1) {
        favoritos.splice(indexFavoritos, 1);
        localStorage.setItem('favoritos', JSON.stringify(favoritos));
    } else if (indexFavoritosRes !== -1) {
        favoritosRes.splice(indexFavoritosRes, 1);
        localStorage.setItem('favoritosRes', JSON.stringify(favoritosRes));
    } else if (indexFavoritosEm !== -1) {
        favoritosEm.splice(indexFavoritosEm, 1);
        localStorage.setItem('favoritosEm', JSON.stringify(favoritosEm));
    }

    // Eliminar el elemento del DOM
    const cardFavorite = event.target.closest('.cardFavorite');
    if (cardFavorite) {
        cardFavorite.remove();
    }
    location.reload();
}

function listaFavoritosServidor() {
    const contenedorFavoritos = document.getElementById('favoritos');
   

    // Realizar las tres llamadas para obtener favoritos de diferentes tipos
    const urls = [
        '/usuarios/Listafavoritos_usuario/restaurantes',
        '/usuarios/Listafavoritos_usuario/emprendimientos',
        '/usuarios/Listafavoritos_usuario/eventos'
    ];

    const camposVacios = container_fav();

    Promise.all(urls.map(url => fetch(url).then(response => response.json())))
        .then(data => {
            const [restaurantes, emprendimientos, eventos] = data;

            // Combinar los resultados de las tres llamadas en un solo array
            const favoritos = [...new Set([...restaurantes.favoritos, ...emprendimientos.favoritos, ...eventos.favoritos])];

            console.log(favoritos);

            if (favoritos.length === 0 && camposVacios ) {
                sinFavoritos('favoritos');
            } else {
                tarjetasFavoritos(favoritos, contenedorFavoritos);
            }

            setTimeout(() => {
                fetch('/usuarios/obtener_favoritos/usuario')
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
            }, 300);
        })
        .catch(error => {
            console.error('Error al obtener los favoritos:', error);
        });
}

function tarjetasFavoritos(data, contenedor) {
    data.forEach(tarjeta => {
        const divTarjeta = document.createElement('div');
        divTarjeta.classList.add('container_tarjeta');

        const contenedorTipoImagen = document.createElement('div');
        contenedorTipoImagen.classList.add('tipo_imagen_container');

        const iconHeart = document.createElement('i');
        iconHeart.classList.add('bi', 'bi-heart-fill', 'favorite');
        iconHeart.style.color = '#cecbcb';
        iconHeart.dataset.id = tarjeta.id;
        iconHeart.dataset.type = tarjeta.tipo;

        const divImagen = document.createElement('div');
        divImagen.classList.add('tipo_imagen');

        const imagen = document.createElement('img');
        imagen.src = tarjeta.logo;
        imagen.alt = `Logo del ${tarjeta.tipo}`;

        const divContenido = document.createElement('div');
        divContenido.classList.add('contenido_texto');

        const nombreRes = document.createElement('p');
        nombreRes.textContent = tarjeta.nombre;

        const divContainer = document.createElement('div');
        divContainer.classList.add('container');

        const divRating = document.createElement('div');
        divRating.classList.add('rating2');

        for (let i = 0; i < 5; i++) {
            const estrella = document.createElement('input');
            estrella.type = 'radio';
            estrella.name = `rating${tarjeta.id}`;
            estrella.setAttribute('style', '--c: #ff9933');
            divRating.appendChild(estrella);
        }

        const divBoton = document.createElement('div');
        divBoton.classList.add('container_btn');

        const enlace = document.createElement('a');
        let urlHtml;
        if (tarjeta.tipo === 'restaurante') {
            urlHtml = '/res/restauranteDetalleServidor';
        } else if (tarjeta.tipo === 'emprendimiento') {
            urlHtml = '/emprende/EmprendeDetalleServidor';
        } else if (tarjeta.tipo === 'evento') {
            urlHtml = '/evento/eventoDetalleServidor';
        }
        enlace.href = `${urlHtml}?id=${tarjeta.id}&tipo=${tarjeta.tipo}`;

        const boton = document.createElement('button');
        boton.classList.add('btn');

        const span1 = document.createElement('span');
        span1.classList.add('btn-text-one');
        span1.textContent = "te interesa";

        const span2 = document.createElement('span');
        span2.classList.add('btn-text-two');
        span2.textContent = "mira más!";

        boton.appendChild(span1);
        boton.appendChild(span2);
        enlace.appendChild(boton);
        divBoton.appendChild(enlace);

        divContainer.appendChild(divRating);

        divContenido.appendChild(nombreRes);
        divContenido.appendChild(divContainer);
        divContenido.appendChild(divBoton);

        divImagen.appendChild(imagen);
        contenedorTipoImagen.appendChild(divImagen);
        contenedorTipoImagen.appendChild(iconHeart);
        divTarjeta.appendChild(contenedorTipoImagen);
        divTarjeta.appendChild(divContenido);

        contenedor.appendChild(divTarjeta);
    });
}

function sinFavoritos(containerFav) {
    const container_fav = document.getElementById(containerFav);
    container_fav.classList.add('container_fav', 'vacio');

    const div_vacío = document.createElement('div');
    div_vacío.classList.add('container_noFav');

    const div_icon = document.createElement('div');
    div_icon.classList.add('div_icon');

    const icon = document.createElement('i');
    icon.classList.add('bi', 'bi-heart');

    const titulo = document.createElement('h2');
    titulo.textContent = 'Aún no tienes listas de favoritos';

    div_icon.appendChild(icon);
    div_vacío.appendChild(div_icon);
    div_vacío.appendChild(titulo);
    container_fav.appendChild(div_vacío);
}
