fetch("http://127.0.0.1:5000")
.then(response => {
    if (!response.ok){
        throw new Error("Ha fallado la API");
    }
    return response.json();
})
.then(data => {
    const tabla = document.getElementById("restaurantes");
    data.forEach(element => {
        const fila = document.createElement("tr");
        const nombre = document.createElement("td");
        const nota = document.createElement("td");
        nombre.style.border = "1px solid black"
        nota.style.border = "1px solid black"
        nota.style.textAlign = "center"
        nombre.textContent = element.Nombre || element.nombre;
        nota.textContent = element.Nota || element.nombre;
        fila.appendChild(nombre);
        fila.appendChild(nota);
        tabla.appendChild(fila);
    });
})
.catch(error => {
    console.error("Error al cargar los datos:", error);
});

const datos = document.getElementById("formulario")

datos.addEventListener("submit", function(e){
    e.preventDefault();

    const data = new FormData(datos)
    
    fetch("http://localhost:5000/insertar_restaurante",{
        method: 'POST',
        body: data
    })
    .then(res => res.json())
    .then(data => {
        console.log("Respuesta del servidor:", data);
        datos.reset()
    })
    .catch(error => {
        console.log("El error ha sido", error);
    })
});


