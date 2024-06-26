document.addEventListener('DOMContentLoaded', () => {
    
    const formularioEm = document.getElementById('formularioLocationEm');
    const btnRegresarEm = document.getElementById('btn_regresarEm');
    const redireccionar = document.getElementById('index').getAttribute('data-url');
    const redireccionarFormEm = document.getElementById('form_emprendimiento').getAttribute('data-url');

    alertaPu(formularioEm,redireccionar,"Registro de publicación exitosa")
    regresarForm(btnRegresarEm,redireccionarFormEm)

})


