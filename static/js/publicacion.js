document.addEventListener('DOMContentLoaded', () => {

    menu_form();
    
    user_sesion().then(() => {
        inicializarBuscador();
    }).catch(error => console.error('Error al inicializar sesión de usuario:', error));



})


