const express = require("express");
const app = express();

const prompt = require("prompt-sync")();
const PORT = prompt('Insertar el puerto el cual quieras tu servidor web:');
const direccion = prompt('Insertar la direccion a la que escucha el servidor:');

app.use(express.static('public'));

app.listen(PORT,() => {
    console.log(`Servidor escuchando en http://${direccion}:${PORT}`)
})

