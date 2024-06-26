document.addEventListener('DOMContentLoaded', () => {

    menu_form();
    
    user_sesion().then(() => {
        inicializarBuscador();
    }).catch(error => console.error('Error al inicializar sesión de usuario:', error));

    const formularioRes = document.getElementById('formularioLocationRes');
    const btnRegresarRes = document.getElementById('btn_regresarRes');
    const redireccionar = document.getElementById('index').getAttribute('data-url');
    const redireccionarFormRes = document.getElementById('form_evento').getAttribute('data-url');

    alertaPu(formularioRes,redireccionar,"Actualización de publicación exitosa")
    regresarForm(btnRegresarRes,redireccionarFormRes)

})


