document.addEventListener('DOMContentLoaded', () => {
    menu_lateral2();

    user_sesion().then(() => {
        inicializarBuscador();
    }).catch(error => console.error('Error al inicializar sesión de administrador:', error));


})