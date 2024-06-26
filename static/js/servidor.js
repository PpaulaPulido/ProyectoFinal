
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
function Categoria(datos, contenedor) {
    // Verificar si se encontraron los datos
    if (datos) {
        // Limpiar el contenido actual del contenedor
        contenedor.innerHTML = '';

        // Iterar sobre la galería de imágenes y crear los elementos <img>
        datos.imagenes.forEach((imagenSrc, index) => {
            // Crear el elemento <img>
            const imagen = document.createElement('img');
            imagen.src = imagenSrc;
            imagen.alt = `Imagen ${index + 1} de ${datos.titulo}`;

            // Crear el elemento div con la clase block
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
            contenedor.appendChild(itemCarousel);
        });
    }
}
function galeria(urlFetch){
    const urlParams = new URLSearchParams(window.location.search);
    const id = urlParams.get('id');
    fetch(`/${urlFetch}/${id}`) 
            .then(response => response.json())
            .then(data => {
                const carouselInner = document.querySelector('.carousel-inner');
                Categoria(data, carouselInner);
                slider_tarjetas();
            })
            .catch(error => {
                console.error('Error al obtener las imágenes:', error);
            });
}

function tarjetasPublicacion(data, contenedor,nombreTipo,altImagen,urlHtml,config) {
   
    data.forEach(tarjeta => {
        const divTarjeta = document.createElement('div');
        divTarjeta.classList.add('container_tarjeta');

        const  contenedorTipoImagen = document.createElement('div');
        contenedorTipoImagen.classList.add('tipo_imagen_container');
        
        const iconHeart = document.createElement('i');
        iconHeart.classList.add('bi', 'bi-heart-fill', 'favorite');
        iconHeart.style.color = '#cecbcb';
        iconHeart.dataset.id = tarjeta[config.id];
        iconHeart.dataset.type = nombreTipo; 

    
        const divImagen = document.createElement('div');
        divImagen.classList.add('tipo_imagen');

        const imagen = document.createElement('img');
        imagen.src = tarjeta[config.logo];
        imagen.alt = altImagen;

        const divContenido = document.createElement('div');
        divContenido.classList.add('contenido_texto');

        const nombreRes = document.createElement('p');
        nombreRes.textContent = tarjeta[config.nombre];

        const divContainer = document.createElement('div');
        divContainer.classList.add('container');

        const divRating = document.createElement('div');
        divRating.classList.add('rating');

        for (let i = 0; i < 5; i++) {
            const estrella = document.createElement('input');
            estrella.type = 'radio';
            estrella.name = 'clr1';
            estrella.setAttribute('style', '--c: #ff9933');
            divRating.appendChild(estrella);
        }

        const divBoton = document.createElement('div');
        divBoton.classList.add('container_btn');

        const enlace = document.createElement('a');
        enlace.href = `${urlHtml}?id=${tarjeta[config.id]}&tipo=${nombreTipo}`;

        
        const boton = document.createElement('button');
        boton.classList.add('btn');

        const span1 = document.createElement('span');
        span1.classList.add('btn-text-one');
        span1.textContent = "te interesa";

        const span2 = document.createElement('span');
        span2.classList.add('btn-text-two');
        span2.textContent = "mira mas!";

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


