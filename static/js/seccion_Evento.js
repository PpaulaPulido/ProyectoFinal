document.addEventListener('DOMContentLoaded', function () {

    const swiper1 = document.getElementById('swiper');
    const swiper2 = document.getElementById('swiper2');
    const detalleEventoUrl = document.getElementById('detalle-evento-url').getAttribute('data-url');

    tarjetas_swiper(datosEventos, swiper1, detalleEventoUrl);
    tarjetas_swiper(eventosTecnologicos, swiper2, detalleEventoUrl);
    manejarFavoritos('favoritos');

    let cardSlider = 3;
    if (window.innerWidth < 920) {
        cardSlider = 1;
    } else if (window.innerWidth < 1024) {
        cardSlider = 2;
    }

    const swiper = new Swiper(".mySwiper", {
        slidesPerView: cardSlider,
        spaceBetween: 20,
        slidesPerGroup: 1,
        loop: true,
        loopFillGroupWithBlank: false,
        navigation: {
            prevEl: ".swiper-button-prev",
            nextEl: ".swiper-button-next",
        }
    });

})




function cargarEventos(tipo) {
    const url = document.getElementById('data-container').getAttribute('data-perfil-url');

    window.location.href = `${url}?tipo=${encodeURIComponent(tipo)}`;
}