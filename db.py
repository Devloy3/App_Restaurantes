from tinydb import TinyDB

class Restaurantes:
    def __init__(self):
        self.db = TinyDB("./db/restaurantes.json")
        self.restaurantes = self.db.table("Restaurantes")

    def crear_1_restaurante(self,nombre,decoracion,menu,comida,servicio,precio):
        restaurante = {
            "Restaurante": nombre,
            "Decoracion": decoracion,
            "Menu": menu,
            "Comida": comida,
            "Servicio": servicio,
            "Precio": precio
        }

        self.restaurantes.insert(restaurante)

    def crear_varios_restaurantes(self, restaurantes):
        self.restaurantes.insert_multiple(restaurantes)

    def mostrar_todos_(self)