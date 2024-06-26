document.addEventListener('DOMContentLoaded', () => {

    menu_form();
    
    user_sesion().then(() => {
        inicializarBuscador();
    }).catch(error => console.error('Error al inicializar sesión de usuario:', error));

    const formulario = document.getElementById('formularioLocation');
    const btnRegresar = document.getElementById('btn_regresar');
    const redireccionar = document.getElementById('index').getAttribute('data-url');
    const redireccionarForm = document.getElementById('form_evento').getAttribute('data-url');


    alertaPu(formulario,redireccionar,"Actualización de publicación exitosa")
    regresarForm(btnRegresar,redireccionarForm)
   

})


