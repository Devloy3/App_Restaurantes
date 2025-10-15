fetch("http://127.0.0.1:5000/mostrar_puntaje")
.then(response => {
    if (!response.ok){
        throw new Error("Ha fallado la API");
    }
    return response.json();
})
.then(data => {
    const tabla = document.getElementById("Varios");
    
    data.forEach(element => {
        const fila = document.createElement("tr");
        const nombre = document.createElement("td");
        const decoracion = document.createElement("td");
        const menu = document.createElement("td");
        const comida = document.createElement("td");
        const servicio = document.createElement("td");
        const precio = document.createElement("td");
        
        nombre.textContent = element.Nombre;
        decoracion.textContent = element.Decoracion;
        menu.textContent = element.Menu;
        comida.textContent = element.Cocina;
        servicio.textContent = element.Servicio;
        precio.textContent = element.Precio;

        nombre.style.border = "1px solid black"
        decoracion.style.border = "1px solid black"
        menu.style.border = "1px solid black"
        comida.style.border = "1px solid black"
        servicio.style.border = "1px solid black"
        precio.style.border = "1px solid black"

        decoracion.style.textAlign = "center"
        menu.style.textAlign = "center"
        comida.style.textAlign = "center"
        servicio.style.textAlign = "center"
        precio.style.textAlign = "center"
        
        
        fila.appendChild(nombre);
        fila.appendChild(decoracion);
        fila.appendChild(menu);
        fila.appendChild(comida);
        fila.appendChild(servicio);
        fila.appendChild(precio);
        tabla.appendChild(fila);
    });
})
.catch(error => {
    console.error("Error al cargar los datos:", error);
});