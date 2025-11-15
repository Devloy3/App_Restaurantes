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
    
    def mostrar_comida(self):
        self.cursor.execute("SELECT * FROM restaurantes ORDER BY Comida")
        comida = self.cursor.fetchall()
        return comida
    
    def mostrar_servicio(self):
        self.cursor.execute("SELECT * FROM restaurantes ORDER BY Servicio")
        servicio = self.cursor.fetchall()
        return servicio
    
    def mostrar_precio(self):
        self.cursor.execute("SELECT * FROM restaurantes ORDER BY Precio")
        precio = self.cursor.fetchall()
        return precio
    
    def promedio_restaurante(self):
        self.cursor.execute("SELECT Restaurante,(Decoracion+Menu+Comida+Servicio+Precio/5) AS Promedio FROM restaurantes")
        promedio = self.cursor.fetchall()
        return promedio
    
    def promedio_total(self):
        self.cursor.execute("SELECT (AVG(Decoracion)+AVG(Menu)+AVG(Comida)+AVG(Servicio)+AVG(Precio)/5) AS promedio_total FROM restaurantes")
        total = self.cursor.fetchall()
        return total
    