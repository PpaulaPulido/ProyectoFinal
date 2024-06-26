document.addEventListener("DOMContentLoaded", function() {
  var pantallaCarga = document.querySelectorAll(".loader-container, .loader-conta");

  pantallaCarga.forEach(function(loaderContainer) {
      loaderContainer.style.display = "flex"; // Ajusta el estilo display según sea necesario
      loaderContainer.style.position = "absolute"; // Cambiado a absolute para cubrir todo el viewport
      loaderContainer.style.animation = "desvanecer 5s ease-in-out forwards";
  });

  setTimeout(function() {
      fadeOut(); // Llama a la función para desvanecer el loader después de 5 segundos (ajusta según necesites)
  }, 5000); // Tiempo en milisegundos antes de desvanecer el loader
});

function fadeOut() {
  var pantallaCarga = document.querySelectorAll(".loader-container, .loader-conta");

  pantallaCarga.forEach(function(loaderContainer) {
      loaderContainer.style.opacity = 1;

      var fadeEffect = setInterval(function () {
          if (!loaderContainer.style.opacity) {
              loaderContainer.style.opacity = 1;
          }
          if (loaderContainer.style.opacity > 0) {
              loaderContainer.style.opacity -= 0.1;
          } else {
              clearInterval(fadeEffect);
              loaderContainer.remove();
          }
      }, 10); // Ajusta la velocidad de desvanecimiento modificando el valor de intervalo
  });
}
