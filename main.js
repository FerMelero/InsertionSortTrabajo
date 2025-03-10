function verificarRespuestas() {
    // Mapa con las respuestas correctas para cada pregunta
    let respuestasCorrectas = {
        "respuesta1": "parís",
        "respuesta2": "roma",
        "respuesta3": "berlín",
        "respuesta4": "madrid",
        "respuesta5": "lisboa"
    };

    let respuestasCorrectasCount = 0;

    // Comprobar si todas las preguntas tienen una respuesta seleccionada
    for (let i = 1; i <= 5; i++) {
        let opciones = document.getElementsByName("respuesta" + i);
        let respuestaUsuario = "";

        // Buscar si alguna opción está seleccionada
        for (let j = 0; j < opciones.length; j++) {
            if (opciones[j].checked) {
                respuestaUsuario = opciones[j].value;
                break;
            }
        }

        // Si no se ha respondido alguna pregunta, mostrar una alerta y salir
        if (respuestaUsuario === "") {
            alert("⚠️ Por favor, responde todas las preguntas antes de enviar.");
            return; // Detener la ejecución si alguna pregunta está sin responder
        }

        let resultado = document.getElementById("resultado" + i);
        let infoBtn = document.getElementById("infoBtn" + i);

        // Comprobar si la respuesta es correcta
        if (respuestaUsuario === respuestasCorrectas["respuesta" + i]) {
            resultado.innerHTML = "✅ ¡Correcto!";
            resultado.style.color = "green";
            respuestasCorrectasCount++;  // Aumentar el contador de respuestas correctas
            infoBtn.style.display = "inline";  // Mostrar el botón de más info
        } else {
            resultado.innerHTML = "❌ Incorrecto. La respuesta correcta es: " + respuestasCorrectas["respuesta" + i];
            resultado.style.color = "red";
            infoBtn.style.display = "none";  // Ocultar el botón de más info si la respuesta es incorrecta
        }
    }

    // Mostrar el resultado final
    alert(`Has acertado ${respuestasCorrectasCount} de 5 respuestas.`);
}

function toggleInfo(preguntaId) {
    const info = document.getElementById(`info${preguntaId}`);
    info.style.display = (info.style.display === "none" || info.style.display === "") ? "block" : "none";
}
