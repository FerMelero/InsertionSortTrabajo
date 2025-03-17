function verificarRespuestas() {
    let respuestasCorrectas = {
        "respuesta1": "p1_3",
        "respuesta2": "p2_2",
        "respuesta3": "p3_1",
        "respuesta4": "p4_2",
        "respuesta5": "p5_2"
    };

    let todasRespondidas = true;

    // Verificar si todas las preguntas han sido respondidas
    for (let i = 1; i <= 5; i++) {
        let opciones = document.getElementsByName("respuesta" + i);
        let respondida = false;

        for (let opcion of opciones) {
            if (opcion.checked) {
                respondida = true;
                break;
            }
        }

        if (!respondida) {
            todasRespondidas = false;
            break;
        }
    }

    if (!todasRespondidas) {
        alert("Por favor, responde todas las preguntas antes de comprobar.");
        return;
    }

    // Evaluar respuestas
    for (let i = 1; i <= 5; i++) {
        let opciones = document.getElementsByName("respuesta" + i);
        let respuestaCorrecta = respuestasCorrectas["respuesta" + i];
        let respuestaUsuario = "";
        let resultado = document.getElementById("resultado" + i);
        let infoBtn = document.getElementById("infoBtn" + i);

        // Resetear colores
        for (let opcion of opciones) {
            let label = document.querySelector(`label[for="${opcion.id}"]`);
            if (label) label.style.color = "black";
        }

        // Obtener la respuesta seleccionada por el usuario
        for (let opcion of opciones) {
            if (opcion.checked) {
                respuestaUsuario = opcion.value;
                break;
            }
        }

        // Evaluar y colorear la respuesta seleccionada
        for (let opcion of opciones) {
            let label = document.querySelector(`label[for="${opcion.id}"]`);
            if (!label) continue;

            if (opcion.checked) {
                if (opcion.value === respuestaCorrecta) {
                    label.style.color = "green"; // Correcta
                    resultado.innerHTML = "¡Correcto!";
                    resultado.style.color = "green";
                    infoBtn.style.display = "inline"; 
                } else {
                    label.style.color = "red"; // Incorrecta
                    resultado.innerHTML = "No es correcto, vuelve a intentarlo.";
                    resultado.style.color = "red";
                    infoBtn.style.display = "none";
                }
            }
        }
    }
}



function toggleInfo(preguntaId) {
    const info = document.getElementById(`info${preguntaId}`);
    // Alternar la visibilidad del texto
    if (info.style.display === "none" || info.style.display === "") {
        info.style.display = "block";  // Mostrar el texto
        info.style.border = "3px solid black";  // Añadir borde negro cuando se muestre
        info.style.padding = "10px";  // Añadir un margen entre el texto y el borde
    } else {
        info.style.display = "none";  // Ocultar el texto
        info.style.border = "";  // Quitar el borde cuando se oculte
        info.style.padding = "";  // Quitar el padding cuando se oculte
    }
}



