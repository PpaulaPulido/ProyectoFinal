//Funcion para la animacion
popupWhatsApp = () =>{
    let btnClosePopup = document.querySelector('.closePopup');   

    let btnOpenPopUp = document.querySelector('.whatsapp-button');      //Abre

    let popup = document.querySelector('.popup-whatsapp');      //Ventana emergente del chat

    let sendBtn = document.getElementById('send-btn');      //getElementById porque es un ID, no una clase

    //addEventListener le asigna eventos a lal variable. Creamos una funcion click qu se inicializa con los parentesis despues de la coma. En los corchetes ponemos lo que queremos que haga la funcion, var popup. El toggle muestra y oculta.
    btnClosePopup.addEventListener("click", ()=>{
        popup.classList.toggle('is-active-whatsapp-popup')      //Clase en whats2.css
    });
    
    btnOpenPopUp.addEventListener("click", ()=>{
        popup.classList.toggle('is-active-whatsapp-popup')
        //Animacion con la hoja de estilos
        popup.style.animation = "fadeIn .6s 0.0s both"      //fadeIn para activarlo. 0.0s el retraso en la animacion. Both es para mostrarlo y cerrarlo
    });

    btnOpenPopUp.addEventListener("click", ()=>{
        let msg = document.getElementById('whats-in')
        msg.value = 'Necesito ayuda'
    });

    sendBtn.addEventListener("click", ()=>{
        let msg = document.getElementById('whats-in').value
        
        window.open('https://wa.me/+573204186199?text=' + msg, '_blank');       //Abre una nueva ventana
    });

    /*setTimeout(() =>{
        popup.classList.toggle('is-active-whatsapp-popup');
    }, 3000);*/
}

popupWhatsApp();