function user_sesion() {
    return fetch('/admin/perfil_imagen')
        .then(response => {
            if (!response.ok) {
                //indica si la solicitud no fue existosa
                throw new Error('Respuesta no fue correcta');
            }
            return response.blob();
        })
        .then(imageBlob => {
            const imagenURL = URL.createObjectURL(imageBlob);
            crearNav(imagenURL)
        })
        .catch(error => {
            //console.error('Error al cargar la imagen del perfil:', error);
            const imagenURL = '/static/img/perfil_user.png'; 
            crearNav(imagenURL);
        });
}

function crearNav(imagenURL) {

    const menuItems = [
        { text: `<img src="${imagenURL}" alt="perfil">`, href: '#', class: 'link1', hasSubMenu: true }
    ];

    const perfilAdminUrl = document.getElementById('data-container').getAttribute('data-perfil-url');
    const adminId = document.getElementById('data-container').getAttribute('data-admin-id');
    const indexUrl = document.getElementById('url_dash').getAttribute('data-url');
    const urlAdminEdit = document.getElementById('url_editarPerfil').getAttribute('data-url');
    const urlCerrarSesion = document.getElementById('url_cerrarSesion').getAttribute('data-url');



    // Elementos del submenu
    const subMenuItems = [
        { text: 'Ver perfil', href: perfilAdminUrl },
        { text: 'Ver dashboard', href: indexUrl },
        { text: 'Configuración', href: urlAdminEdit },
        { text: 'Cerrar sesión', href: urlCerrarSesion }
    ];

    const nav_user = document.createElement('nav');
    nav_user.className = 'barra_nav';

    const nav_list = document.createElement('ul');
    nav_list.className = 'nav_list';

    crearBuscadorNav(nav_list)
    crearMenuItem(nav_list, menuItems, subMenuItems);

    nav_user.appendChild(nav_list);

    const header_barra = document.createElement('div');
    header_barra.id = "header_barra";
    header_barra.appendChild(nav_user);

    const header = document.querySelector('#cabeza');
    header.appendChild(header_barra);

    const cerrarSesionElement = nav_list.querySelector('a[href="' + urlCerrarSesion + '"]');
    cerrarSesionElement.addEventListener('click', function(event) {
        event.preventDefault(); 
        Swal.fire({
            position: "center",
            icon: "success",
            title: "Cerrando sesión...",
            showConfirmButton: false,
            timer: 2000,
            customClass: {
                confirmButton: 'btn-red',
                popup: 'border-blue swal2-popup-custom',
                title: 'swal2-title',
                icon: 'icon-swal',
                container: 'custom-container'
            }
        });
        setTimeout(function() {
            window.location.href = 'http://127.0.0.1:3036/' // Redirigir a la página de inicio
        }, 2000);
        
    });
}

function crearBuscadorNav(nav_list) {

    // Crear elemento li para el buscador
    const buscador_li = document.createElement('li');
    buscador_li.innerHTML = `
        <div class="header_buscador">
            <div class="buscador_input">
                <div id="ctn-bars-search">
                    <input type="text" id="inputSearch" placeholder="¿Qué deseas buscar?">
                </div>
                <div id="ctn-icon-search">
                    <i class="fas fa-search" id="icon-search"></i>
                </div>
            </div>
            <ul id="box-search"></ul>
            <div id="cover-ctn-search"></div>
        </div>`;
    nav_list.appendChild(buscador_li);

    const icon_a = document.createElement('a');
    icon_a.classList.add('enlace_icon');
    icon_a.href = '#';

    const icon = document.createElement('i');
    icon.classList.add('bi', 'bi-bell-fill');

    icon_a.appendChild(icon);
    nav_list.appendChild(icon_a);
}

function crearMenuItem(nav_list, menuItems, subMenuItems) {
    // Crear elementos li y a para el menú principal
    menuItems.forEach(item => {
        const liElement = document.createElement('li');
        if (item.hasSubMenu) {
            const aElement = document.createElement('a');
            aElement.className = item.class;
            aElement.href = item.href;
            aElement.innerHTML = item.text;
            liElement.appendChild(aElement);
            const subMenu = document.createElement('ul');
            subMenu.className = 'perfil_list';
            subMenuItems.forEach(subItem => {
                const subLiElement = document.createElement('li');
                const subAElement = document.createElement('a');
                subAElement.href = subItem.href;
                subAElement.textContent = subItem.text;
                subLiElement.appendChild(subAElement);
                subMenu.appendChild(subLiElement);
            });
            liElement.appendChild(subMenu);

        } else {
            const aElement = document.createElement('a');
            aElement.className = item.class;
            aElement.href = item.href;
            aElement.textContent = item.text;
            liElement.appendChild(aElement);
        }
        nav_list.appendChild(liElement);
    });
}

function menu_lateral() {
    // sidebar toggle
    const btnToggle = document.querySelector('.toggle-btn');

    btnToggle.addEventListener('click', function () {
        document.getElementById('sidebar').classList.toggle('active');
        document.getElementById('publicaciones').classList.toggle('active');
        console.log(document.getElementById('sidebar'))
    });
}

function menu_lateral2() {
    // sidebar toggle
    const btnToggle = document.querySelector('.toggle-btn');

    btnToggle.addEventListener('click', function () {
        document.getElementById('sidebar').classList.toggle('active');
        console.log(document.getElementById('sidebar'))
    });
}

function menu_form(){

    const btnToggle = document.querySelector('.toggle-btn');

    btnToggle.addEventListener('click', function () {
        document.getElementById('sidebar').classList.toggle('active');
        document.getElementById('publicaciones__form').classList.toggle('active');
        console.log(document.getElementById('sidebar'))
    });
}


function regresarForm(btnRegresar,redireccionarForm){
    btnRegresar.addEventListener('click', () => {
        Swal.fire({
            title: "¿Estás seguro de que deseas regresar?",
            text: "Si regresas, podrías tener que reingresar algunos datos.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Sí, deseo regresar!",
            cancelButtonText: "Cancelar",
            customClass: {
                confirmButton: 'btn-blue',
                popup: 'border-blue',
                title: 'title-swal',
                icon: 'icon-swal',
            }
        }).then((result) => {
            if (result.isConfirmed) {
                // Si el usuario confirma, redirigir a la página especificada
                Swal.fire({
                    title: "Volviste al formulario anterior",
                    text: "Verifica los datos antes de continuar",
                    icon: "info",
                    timer: 4000,
                    customClass: {
                        confirmButton: 'btn-blue',
                        popup: 'border-blue',
                        title: 'title-swal',
                        icon: 'icon-swal',
                    }
                }).then(() => {

                    window.location.href = redireccionarForm;
                });

            } else {
                // Si el usuario cancela, simplemente cerrar la alerta y permanecer en la página
                Swal.fire({
                    title: "Cancelado",
                    text: "Continúa con el formulario actual.",
                    icon: "info",
                    timer: 2000,
                    customClass: {
                        popup: 'border-blue',
                        icon: 'success-icon',
                    }
                });
            }
        });
    });

}
function alertaPu(formulario, redireccionar,message) {
    formulario.addEventListener('submit', (e) => {
        e.preventDefault(); // Prevenir el envío del formulario por defecto

        // Mostrar la alerta de SweetAlert
        Swal.fire({
            position: "center",
            icon: "success",
            title: message,
            showConfirmButton: false,
            timer: 2000,
            customClass: {
                popup: 'border-blue', // Clase CSS para el borde del SweetAlert
                icon: 'success-icon',
            }
        }).then(() => {
            // Crear un objeto FormData con los datos del formulario
            const formData = new FormData(formulario);

            // Enviar el formulario manualmente usando fetch
            fetch(formulario.action, {
                method: 'POST',
                body: formData
            }).then(response => {
                if (response.ok) {
                    // Después de que el formulario se envíe, redirigir a la página especificada
                    setTimeout(() => {
                        window.location.href = redireccionar;
                    }, 1000); // Retardo adicional de 1 segundo (1000 milisegundos)
                } else {
                    // Manejar el error de envío
                    console.error('Error al enviar el formulario:', response.statusText);
                }
            }).catch(error => {
                // Manejar errores de red
                console.error('Error de red al enviar el formulario:', error);
            });
        });
    });
}
