import sqlite3
from db.db import NoRelacional

conn = sqlite3.connect("restaurantes.db")
cursor = conn.cursor()


tablas = ''' CREATE TABLE restaurantes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Restaurante VARCHAR(100),
    Decoracion DECIMAL(5,1),
    Menu DECIMAL(5,1),
    Comida DECIMAL(5,1),
    Servicio DECIMAL(5,1),
    Precio DECIMAL(5,1)
);

CREATE TABLE localizaciones(
    latitud FLOAT,
    longitud FLOAT,
    id_restaurante INTEGER,
    FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id)
);'''

cursor.executescript(tablas)
datos = NoRelacional.mostrar_todos()

for Restaurante,Decoracion,Menu,Comida,Servicio,Precio in datos:
    cursor.execute("INSERT INTO restaurantes(Restaurante,Decoracion,Menu,Comida,Servicio,Precio) VALUES(?,?,?,?,?,?)", (Restaurante,Decoracion,Menu,Comida,Servicio,Precio))

conn.commit()