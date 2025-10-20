import sqlite3
from datetime import date
from db.db import NoRelacional

class Relacional:
    def __init__(self):
        self.conn = sqlite3.connect("./db/nota_media.db")
        self.cursor = self.conn.cursor()
    
    def construir_tabla(self):
        self.cursor.execute(
            '''
        CREATE TABLE notas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Fecha DATE,
        Nota_media INT);'''
        )

    def insertar_datos(self):
        notas = NoRelacional.mostar_el_promedio_total()
        fecha = date.today()
        fecha_string = fecha.strftime("%y-%m-%d")

        self.cursor.execute("SELECT Nota_media FROM notas WHERE Fecha = ?", (fecha_string,))
        resultado = self.cursor.fetchone()

        if resultado is None or resultado[0] != notas:
            self.cursor.execute("INSERT INTO notas(Fecha, Nota_media) VALUES (?, ?);", (fecha_string, notas))
            self.conn.commit()
            print("Datos insertados.")
        else:
            print("La nota ya está registrada para esta fecha. No se insertó nada.")

    def mostrar_todos_los_datos(self):
        self.cursor.execute("SELECT * FROM notas")
        resultados = self.cursor.fetchall()
        notas_fecha = []
        for notas,dia in resultados:
            notas_fecha.append({"Nota": notas, "Fecha": dia})
        
        return notas_fecha
    

    