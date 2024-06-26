document.addEventListener('DOMContentLoaded', function () {

    const swiper = document.getElementById('swiper');
    const swiper2 = document.getElementById('swiper2');
    const detalleEmprendeUrl = document.getElementById('detalle-emprende-url').getAttribute('data-url');
    
    tarjetas_swiper(datosEmpredimientos, swiper,detalleEmprendeUrl);
    tarjetas_swiper(empredimientosArtesania, swiper2,detalleEmprendeUrl);
    manejarFavoritos('favoritosEm');

    let cardSlider = 3;
    if (window.innerWidth < 920) {
        cardSlider = 1;
    } else if (window.innerWidth < 1024) {
        cardSlider = 2;
    }

    const swiper3 = new Swiper(".mySwiper", {
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
});


