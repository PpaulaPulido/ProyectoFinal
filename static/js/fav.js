//funciones generales

function manejarFavoritos(sectionKey) {
    const hard_favorites = document.querySelectorAll('.bi-heart-fill');
    let listaFavoritos = [];

    const getFavorites = localStorage.getItem(sectionKey);
    if (getFavorites) {
        listaFavoritos = JSON.parse(getFavorites);
    }

    hard_favorites.forEach(function (hard_favorite) {
        const eventId = hard_favorite.getAttribute('data-event-id');

        // Establecer el estado inicial de los elementos favoritos
        if (listaFavoritos.includes(eventId)) {
            hard_favorite.classList.add('checked');
        }

        hard_favorite.addEventListener('click', function () {
            if (!hard_favorite.classList.contains('checked')) {
                hard_favorite.classList.add('checked');
                listaFavoritos.push(eventId);
            } else {
                hard_favorite.classList.remove('checked');
                listaFavoritos = listaFavoritos.filter(id => id !== eventId);
            }
            localStorage.setItem(sectionKey, JSON.stringify(listaFavoritos));
        });
    });
}

function Categoria(typeEvento, id) {

    // Obtener el contenedor donde se agregarán las imágenes
    const carouselInner = document.querySelector('.carousel-inner');


    // Buscar los datos correspondientes al ID e window.datosEventos
    const datosEventos = typeEvento.find(tarjeta => tarjeta.id === parseInt(id));

    // Verificar si se encontraron los datos
    if (datosEventos) {
        // Limpiar el contenido actual del carrusel
        carouselInner.innerHTML = '';

        // Iterar sobre la galería de imágenes y crear los elementos <img>
        datosEventos.galeria.forEach((imagenSrc, index) => {
            // Crear el elemento <img>
            const imagen = document.createElement('img');
            imagen.src = imagenSrc;
            imagen.alt = `Imagen ${index + 1} de ${datosEventos.titulo}`;

            //crear elemendo div con la clase blck
            const block = document.createElement('div');
            block.classList.add('block', 'img-responsive');
            block.appendChild(imagen);

            // Crear el elemento <div class="carousel-col"> y agregar la imagen
            const carouselCol = document.createElement('div');
            carouselCol.classList.add('carousel-col');
            carouselCol.appendChild(block);

            // Crear el elemento <div class="item"> y agregar la columna del carrusel
            const itemCarousel = document.createElement('div');
            itemCarousel.classList.add('item');
            if (index === 0) {
                itemCarousel.classList.add('active'); // Marcar el primer elemento como activo
            }
            itemCarousel.appendChild(carouselCol);

            // Agregar el elemento <div class="item"> al contenedor principal del carrusel
            carouselInner.appendChild(itemCarousel);
        });
    }
}

function slider_tarjetas() {
    $('.carousel[data-type="multi"] .item').each(function () {
        var next = $(this).next();
        if (!next.length) {
            next = $(this).siblings(':first');
        }
        next.children(':first-child').clone().appendTo($(this));

        for (var i = 0; i < 2; i++) {
            next = next.next();
            if (!next.length) {
                next = $(this).siblings(':first');
            }

            next.children(':first-child').clone().appendTo($(this));
        }
    });
}
function tarjetas_swiper(tarjeta, contenedor,enlace) {

    tarjeta.forEach(function (dato) {

        const card_swiper = document.createElement("div");
        card_swiper.classList.add("swiper-slide", "card");

        const card_content = document.createElement("div");
        card_content.classList.add("card-content");

        const content_title = document.createElement('div');
        content_title.classList.add('title_contenedor');

        const card_title = document.createElement("h2");
        card_title.classList.add("content_title");
        card_title.textContent = dato.titulo;

        const card_imagen = document.createElement("div");
        card_imagen.classList.add("swiper_img");

        const card_img = document.createElement("img");
        card_img.classList.add("card_img");
        card_img.src = dato.galeria[3];
        card_img.alt = `imagen ${dato.titulo}`;

        const container_div = document.createElement("div");
        container_div.classList.add("swiper_conta_img");

        const favorite = document.createElement('i');
        favorite.classList.add("bi", "bi-heart-fill", "favorite");
        favorite.setAttribute('data-event-id', dato.id);

        const rating = document.createElement('div');
        rating.classList.add("rating");

        let a = document.createElement("a");
        a.classList.add('swiper_button');
        a.href = `${enlace}?id=${dato.id}`;
        a.textContent = "Ver más";

        for (let i = 0; i < 5; i++) {
            const star = document.createElement('i');
            star.classList.add("bi", "bi-star-fill", "star");
            rating.appendChild(star);
        }

        card_imagen.appendChild(card_img);
        container_div.appendChild(card_imagen);
        container_div.appendChild(favorite);

        card_content.appendChild(container_div);
        content_title.appendChild(card_title);
        card_content.appendChild(content_title);
        card_content.appendChild(rating);
        card_content.appendChild(a);
        card_swiper.appendChild(card_content);
        contenedor.appendChild(card_swiper);

    });
}