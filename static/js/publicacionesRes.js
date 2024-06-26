document.addEventListener('DOMContentLoaded', () => {

    
    const formularioRes = document.getElementById('formularioLocationRes');
    const btnRegresarRes = document.getElementById('btn_regresarRes');
    const redireccionar = document.getElementById('index').getAttribute('data-url');
    const redireccionarFormRes = document.getElementById('form_res').getAttribute('data-url');

    alertaPu(formularioRes,redireccionar,"Registro de publicación exitosa")
    regresarForm(btnRegresarRes,redireccionarFormRes)
})


