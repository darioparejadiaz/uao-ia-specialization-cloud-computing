document.getElementById("colorButton").addEventListener("click", function() {
    // Cambia el color de fondo a un color aleatorio
    const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
    document.body.style.backgroundColor = randomColor;
});