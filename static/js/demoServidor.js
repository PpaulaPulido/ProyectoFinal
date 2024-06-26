document.addEventListener('DOMContentLoaded', function () {
    /**
 * Calcula y muestra los detalles de la dirección para múltiples direcciones
 * basado en un texto de formato libre
 *
 * @param  {H.service.Platform} platform   Una clase simulada para acceder a los servicios de HERE
 * 
 */
    function geocode(platform) {
        if (!platform || !(platform instanceof H.service.Platform)) {
            console.error('Plataforma no válida.');
            return;
        }
    
        const geocoder = platform.getSearchService();
        const urlParams = new URLSearchParams(window.location.search);
        const eventId = parseInt(urlParams.get('id'));
        const tipo = urlParams.get('tipo');
    
        if (isNaN(eventId) || !tipo) {
            console.error('Parámetros de URL no válidos.');
            return;
        }
    
        function fetchDataAndGeocode(typeData, id) {
            fetch(`/publicacion/${typeData}/${id}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Error en la respuesta del servidor');
                    }
                    return response.json();
                })
                .then(data => {
                    if (data && Array.isArray(data)) {
                        let hasLocations = false;
                        data.forEach(item => {
                            if (item.ubicacion) {
                                hasLocations = true;
                                const geocodingParameters = { q: item.ubicacion };
                                geocoder.geocode(geocodingParameters, onSuccess, onError);
                            }
                        });
                        if (!hasLocations) {
                            // No hay ubicaciones en los datos
                            document.getElementById('location').textContent = 'No hay direcciones para mostrar';
                        }
                    } else {
                        console.error('Datos de ubicación no válidos:', data);
                    }
                })
                .catch(error => {
                    console.error('Error al obtener las ubicaciones:', error);
                });
        }
    
    
        if (tipo === 'restaurante') {
            fetchDataAndGeocode('restaurante/ubicacion', eventId);
        } else if (tipo === 'evento') {
            fetchDataAndGeocode('evento/ubicacion', eventId);
        } else if (tipo === 'emprendimiento') {
            fetchDataAndGeocode('emprendimiento/ubicacion', eventId);
        } else {
            console.error('Tipo no válido:', tipo);
        }
    }
    

    /**
     * Esta función se llamará una vez que el servicio Geocoder REST proporcione una respuesta
     * @param  {Object} result Un objeto JSON que representa la(s) ubicación(es) encontrada(s).
     * Ver: https://www.here.com/docs/bundle/geocoding-and-search-api-v7-api-reference/page/index.html#/paths/~1geocode/get
     */
    function onSuccess(result) {
        var locations = result.items;
        addLocationsToMap(locations);
        addLocationsToPanel(locations);
        // ... etc.
    }

    /**
     * Esta función se llamará si ocurre un error de comunicación durante la solicitud JSON-P
     * @param  {Object} error  El mensaje de error recibido.
     */
    function onError(error) {
        alert('No se puede alcanzar el servidor remoto' + error);
    }

    /**
     * El código de inicialización del mapa comienza a continuación:
     */

    // Paso 1: inicializa la comunicación con la plataforma
    // En tu propio código, reemplaza la variable window.apikey con tu propia apikey
    var platform = new H.service.Platform({
        apikey: 'EPjM1bMX0FYwE_3K5CLwBNjDVKMa7ODSRH4yJO8Dm9g'
    });
    var defaultLayers = platform.createDefaultLayers();


    var map = new H.Map(document.getElementById('map'),
        defaultLayers.vector.normal.map, {
        center: { lat: 37.376, lng: -122.034 },
        zoom: 15,
        pixelRatio: window.devicePixelRatio || 1
    });
    // añade un oyente de cambio de tamaño para asegurarse de que el mapa ocupa todo el contenedor
    window.addEventListener('resize', () => map.getViewPort().resize());

    var locationsContainer = document.getElementById('panel');

    // Paso 3: hace el mapa interactivo
    // MapEvents habilita el sistema de eventos
    // Behavior implementa interacciones predeterminadas para pan/zoom (también en entornos táctiles móviles)
    var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

    // Crea los componentes de la interfaz de usuario predeterminados
    var ui = H.ui.UI.createDefault(map, defaultLayers);

    // Mantiene una referencia a cualquier infobubble abierto
    var bubble;

    /**
     * Abre/Cierra un infobubble
     * @param  {H.geo.Point} position     La ubicación en el mapa.
     * @param  {String} text              El contenido del infobubble.
     */
    function openBubble(position, text) {
        if (!bubble) {
            bubble = new H.ui.InfoBubble(
                position,
                { content: text });
            ui.addBubble(bubble);
        } else {
            bubble.setPosition(position);
            bubble.setContent(text);
            bubble.open();
        }
    }

    /**
     * Crea una serie de elementos de lista para cada ubicación encontrada y los agrega al panel.
     * @param {Object[]} locations Un array de ubicaciones tal como se recibe del
     *                             servicio H.service.GeocodingService
     */
    function addLocationsToPanel(locations) {
        var nodeOL = document.createElement('ul');
        nodeOL.style.fontSize = 'small';
        nodeOL.style.marginLeft = '5%';
        nodeOL.style.marginRight = '5%';

        for (var i = 0; i < locations.length; i++) {
            var location = locations[i];
            var li = document.createElement('li');
            var divLabel = document.createElement('div');
            var address = location.address;
            var content = '<strong style="font-size: large;">' + address.label + '</strong></br>';
            var position = location.position;

            content += '<strong>Número de casa:</strong> ' + address.houseNumber + '<br/>';
            content += '<strong>Calle:</strong> ' + address.street + '<br/>';
            content += '<strong>Distrito:</strong> ' + address.district + '<br/>';
            content += '<strong>Ciudad:</strong> ' + address.city + '<br/>';
            content += '<strong>Código Postal:</strong> ' + address.postalCode + '<br/>';
            content += '<strong>Condado:</strong> ' + address.county + '<br/>';
            content += '<strong>País:</strong> ' + address.countryName + '<br/>';
            content += '<strong>Posición:</strong> ' +
                Math.abs(position.lat.toFixed(4)) + ((position.lat > 0) ? 'N' : 'S') +
                ' ' + Math.abs(position.lng.toFixed(4)) + ((position.lng > 0) ? 'E' : 'W') + '<br/>';

            divLabel.innerHTML = content;
            li.appendChild(divLabel);
            nodeOL.appendChild(li);
        }

        //locationsContainer.appendChild(nodeOL);
    }

    /**
     * Crea una serie de H.map.Markers para cada ubicación encontrada y los agrega al mapa.
     * @param {Object[]} locations Un array de ubicaciones tal como se recibe del
     *                             servicio H.service.GeocodingService
     */
    function addLocationsToMap(locations) {
        var group = new H.map.Group();

        for (var i = 0; i < locations.length; i++) {
            var location = locations[i];
            var marker = new H.map.Marker(location.position);
            marker.label = location.address.label;
            group.addObject(marker);
        }

        group.addEventListener('tap', function (evt) {
            map.setCenter(evt.target.getGeometry());
            openBubble(evt.target.getGeometry(), evt.target.label);
        }, false);

        map.addObject(group);
        map.setCenter(group.getBoundingBox().getCenter());
    }

    // Ahora usa el mapa según sea necesario...
    geocode(platform);

})