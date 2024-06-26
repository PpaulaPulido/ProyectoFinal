document.addEventListener('DOMContentLoaded', function () {

    resenasUsu()
    galeryMin()

});
function Myphotos() {

    fetch('/usuarios/MisFotosUsuario')
        .then(response => response.json())  // Parsear la respuesta como JSON
        .then(fotos => {

            const photo = document.getElementById('opciones__resultado');

            // Limpiar el contenido anterior de la galería
            photo.innerHTML = '';

            if (fotos.length === 0) {
                // No hay fotos, mostrar un mensaje
                photo.style.display = 'block';

                containerDatosVacio(photo,"/static/img/camara.png","No hay fotos para mostrar");
            
            } else {
                // Hay fotos, mostrarlas
                photo.style.display = 'grid';
                fotos.forEach(foto => {

                    const divImg = document.createElement('div');
                    divImg.classList.add('divImgPhotos');

                    const imgGaleria = document.createElement('img');
                    imgGaleria.src = foto.ruta_foto;
                    imgGaleria.alt = 'Foto ' + foto.tipo_foto;
                    imgGaleria.classList.add('imgPhotos');

                    divImg.appendChild(imgGaleria);
                    photo.appendChild(divImg);
                });

            }
        })
        .catch(error => {
            console.error('Error al cargar las fotos:', error);
        });
}
function galeryMin() {
    fetch('/usuarios/galeriaUsuario')
        .then(response => response.json())  // Parsear la respuesta como JSON
        .then(fotos => {
            const galeria = document.getElementById('galeria');

            // Limpiar el contenido anterior de la galería
            galeria.innerHTML = '';

            if (fotos.length === 0) {
                // No hay fotos, mostrar un mensaje
                galeria.style.display = 'block';
                sinDatos(galeria, 'fa-solid', 'fa-camera-retro')

            } else {
                // Hay fotos, mostrarlas
                galeria.style.display = 'grid';
                fotos.forEach(foto => {
                    const imgGaleria = document.createElement('img');
                    imgGaleria.src = foto.ruta_foto;
                    imgGaleria.alt = 'Foto ' + foto.tipo_foto;
                    imgGaleria.classList.add('imgGaleria');
                    galeria.appendChild(imgGaleria);
                });
            }
        })
        .catch(error => {
            console.error('Error al cargar las fotos:', error);
        });
}
function resenasUsu() {

    fetch('/usuarios/reseñasUsuario')
        .then(response => response.json())  
        .then(resenas => {

            const resena = document.getElementById('opciones__resultado');

            // Limpiar el contenido anterior de la galería
            resena.innerHTML = '';

            if (resenas.length == 0) {
                resena.style.display = 'block';

                containerDatosVacio(resena,"/static/img/resenas.jpg","No hay reseñas para mostrar");
            
            } else {
                resena.style.display = 'grid';
            }
        })
        .catch(error => {
            console.error('Error al cargar las reseñas:', error);
        });
}

function sinDatos(container, icon1, icon2) {

    const containerPhoto = document.createElement('div');
    containerPhoto.classList.add('containerPhoto');

    const containerIcon = document.createElement('div');
    containerIcon.classList.add('iconContainer');

    const iconPhoto = document.createElement('i');
    iconPhoto.classList.add(`${icon1}`, `${icon2}`);

    const textPhoto = document.createElement('p');
    textPhoto.className = "textPhoto";
    textPhoto.textContent = "No hay fotos para mostrar";

    containerIcon.appendChild(iconPhoto);
    containerPhoto.appendChild(containerIcon);
    containerPhoto.appendChild(textPhoto);

    container.appendChild(containerPhoto);
}
function containerDatosVacio(container,urlImg,texto) {

    const containerPhoto = document.createElement('div');
    containerPhoto.classList.add('containerMyPhotos');

    const containerImg = document.createElement('div');
    containerImg.classList.add('MyphotosImg');

    const img = document.createElement('img');
    img.className = "imgPhoto"
    img.src = `${urlImg}`;

    const textPhoto = document.createElement('p');
    textPhoto.className = "textPhotoImg";
    textPhoto.textContent = `${texto}`;

    containerImg.appendChild(img);
    containerPhoto.appendChild(containerImg);
    containerPhoto.appendChild(textPhoto);

    container.appendChild(containerPhoto);
}