document.addEventListener('DOMContentLoaded', () => {
    menu();
    
    user_sesion().then(() => {
        inicializarBuscador();
    }).catch(error => console.error('Error al inicializar sesión con administrador:', error));

});

function menu() {
    // sidebar toggle
    const btnToggle = document.querySelector('.toggle-btn');

    btnToggle.addEventListener('click', function () {
        document.getElementById('sidebar').classList.toggle('active');
        document.getElementById('contenedorPerfil').classList.toggle('active');
        console.log(document.getElementById('sidebar'))
    });
}