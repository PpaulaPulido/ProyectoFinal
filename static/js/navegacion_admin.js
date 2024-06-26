document.addEventListener('DOMContentLoaded',()=>{
    user_sesion().then(() => {
        inicializarBuscador();
    }).catch(error => console.error('Error al inicializar sesión de usuario:', error));
})