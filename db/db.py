import sqlite3

class Relacional:
    def __init__(self):
        self.conn = sqlite3.connect("restaurantes.db")
        self.cursor = self.conn.cursor()

    def crear_restaurante(self,nombre,decoracion,menu,comida,servicio,precio):
        self.cursor.execute("INSERT INTO restaurante(Restaurante,Decoracion,Menu,Comida,Servicio,Precio) VALUES (?,?,?,?,?,?)", (nombre,decoracion,menu,comida,servicio,precio))
        self.conn.commit()
    
    def mostrar_restaurantes(self):
        self.cursor.execute("SELECT * FROM restaurantes")
        todo = self.cursor.fetchall()
        return todo
    
    def mostrar_decoracion(self):
        self.cursor.execute("SELECT * FROM restaurantes ORDER BY Decoracion")
        decoracion = self.cursor.fetchall()
        return decoracion
    
    def mostrar_menu(self):
        self.cursor.execute("SELECT * FROM restaurantes ORDER BY Menu")
        menu = self.cursor.fetchall()
        return menu
    
