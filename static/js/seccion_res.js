document.addEventListener('DOMContentLoaded', function () {

    const swiper = document.getElementById('swiper');
    const swiper2 = document.getElementById('swiper2');
    const swiper3 = document.getElementById('swiper3');

    const detalleResUrl = document.getElementById('detalle-res-url').getAttribute('data-url');

    tarjetas_swiper(datosTarjetas, swiper, detalleResUrl);
    tarjetas_swiper(restaurantesTematicos, swiper2, detalleResUrl);
    tarjetas_swiper(restaurantesVista, swiper3, detalleResUrl);
    manejarFavoritos('favoritosRes');

    let cardSlider = 3;
    if (window.innerWidth < 920) {
        cardSlider = 1;
    } else if (window.innerWidth < 1024) {
        cardSlider = 2;
    }

    const swiper4 = new Swiper(".mySwiper", {
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




