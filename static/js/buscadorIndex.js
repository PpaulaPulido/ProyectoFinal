function inicializarBuscador() {
    let bars_search = document.getElementById("ctn-bars-search");
    let cover_ctn_search = document.getElementById("cover-ctn-search");
    let inputSearch = document.getElementById("inputSearch");
    let box_search = document.getElementById("box-search");
    let search = document.getElementById('ctn-icon-search');

    document.getElementById("icon-search").addEventListener("click", mostrarAlertaBuscadorDeshabilitado);
    document.getElementById("cover-ctn-search").addEventListener("click", ocultar_buscador);

    // Aquí se agrega la funcionalidad para mostrar la alerta cuando se presiona Enter
    inputSearch.addEventListener("keyup", function (event) {
        if (event.key === 'Enter') {
            mostrarAlertaBuscadorDeshabilitado();
        }
    });

    // Aquí se agrega la funcionalidad para mostrar la alerta cuando se hace clic en el botón de búsqueda
    search.addEventListener('click', () => {
        mostrarAlertaBuscadorDeshabilitado();
    });

    function mostrar_buscador() {
        bars_search.style.top = "80px";
        cover_ctn_search.style.display = "block";
        inputSearch.focus();

        box_search.innerHTML = '';

        if (inputSearch.value === "") {
            box_search.style.display = "none";
        }
    }

    function ocultar_buscador() {
        bars_search.style.top = "-10px";
        cover_ctn_search.style.display = "none";
        inputSearch.value = "";
        box_search.style.display = "none";
    }

    function mostrarAlertaBuscadorDeshabilitado() {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: "Lo sentimos, el buscador se encuentra deshabilitado para el público!",
            customClass: {
                confirmButton: 'btn-blue',
                popup: 'border-blue',
                title: 'title-swal',
                icon: 'icon-swal',
            }

        });
    }

    document.getElementById("inputSearch").addEventListener("keyup", buscador_interno);

    function buscador_interno() {
        let filter = inputSearch.value.toUpperCase();
        let li = box_search.getElementsByTagName("li");

        for (let i = 0; i < li.length; i++) {
            let a = li[i].getElementsByTagName("a")[0];
            let textValue = a.textContent || a.innerText;

            if (textValue.toUpperCase().indexOf(filter) > -1) {
                li[i].style.display = "";
                box_search.style.display = "block";
            } else {
                li[i].style.display = "none";
            }

            if (inputSearch.value === "") {
                box_search.style.display = "none";
            }
        }
    }
}
