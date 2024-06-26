document.addEventListener('DOMContentLoaded',()=>{

    menuToggle();
    user_sesion().then(() => {
        inicializarBuscador();
    }).catch(error => console.error('Error al inicializar sesión de usuario:', error));
})

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
        console.error('Error al cargar la imagen del perfil:', error);
        const imagenURL = '/static/img/perfil_user.png'; 
        crearNav(imagenURL);
    });
    
}

function crearNav(imagenURL){

    const urlNosotros = document.getElementById('url_nosotros').getAttribute('data-url');
    const urlIndex = document.getElementById('url_index').getAttribute('data-url');
    const urlFavoritos = document.getElementById('url_favoritos').getAttribute('data-url');
    const urlPerfil = document.getElementById('url_perfil').getAttribute('data-url');
    const urlEditarPerfil = document.getElementById('url_editarPerfil').getAttribute('data-url');
    const urlDasboard = document.getElementById('url_dashboard').getAttribute('data-url');
    const urlcerrarSesion = document.getElementById('url_cerrarSesion').getAttribute('data-url');

    const menuItems = [
        { text: 'Sobre Nosotros', href: urlNosotros, class: 'link' },
        { text: 'Inicio', href: urlIndex, class: 'link' },
        { text: 'Mis favoritos', href: urlFavoritos, class: 'link' },
        { text: `<img src="${imagenURL}" alt="perfil" id= "fotoPerfilNav">`, href: '#', class: 'link1', hasSubMenu: true }
    ];

    // Elementos del submenu
    const subMenuItems = [
        { text: 'Ver perfil', href: urlPerfil },
        { text: 'Ver dashboard', href: urlDasboard},
        { text: 'Configuración', href: urlEditarPerfil},
        { text: 'Cerrar sesión', href: urlcerrarSesion }
    ];

    const nav_user = document.createElement('nav');
    nav_user.className = 'barra_nav';

    const nav_list = document.createElement('ul');
    nav_list.className = 'nav_list';

    crearBuscadorNav(nav_list);
    crearMenuItem(nav_list,menuItems,subMenuItems);
    // Agregar nav_list a nav_user
    nav_user.appendChild(nav_list);

    const header_barra = document.createElement('div');
    header_barra.id = "header_barra";
    header_barra.appendChild(nav_user);

    const header = document.querySelector('#cabeza');
    header.appendChild(header_barra);

    const cerrarSesionElement = nav_list.querySelector('a[href="' + urlcerrarSesion + '"]');
    cerrarSesionElement.addEventListener('click', function(event) {
        event.preventDefault(); 
        Swal.fire({
            position: "top-end",
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
function crearBuscadorNav(nav_list){
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
}
function crearMenuItem(nav_list,menuItems,subMenuItems){
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

function menuToggle(){
    const mobileMenu = document.getElementById('mobile-menu');
        const navList = document.getElementById('nav-list2');
        const cerrar = document.getElementById('cerrar');

        document.addEventListener('click', function (event) {
            // Comprobar si el clic no fue dentro del menú o el botón de toggle
            if (!navList.contains(event.target) && !mobileMenu.contains(event.target)) {
                // Cerrar el menú
                navList.classList.remove('active');
                mobileMenu.classList.remove('is-active');
            }
        });

        mobileMenu.addEventListener('click', () => {

            navList.classList.toggle('active');
            mobileMenu.classList.toggle('is-active');
        });

        cerrar.addEventListener('click', () => {
            navList.style.transition = 'left 0.9s ease';
            navList.classList.remove('active');
            mobileMenu.classList.remove('is-active');
        })
}