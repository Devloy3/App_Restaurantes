from tinydb import TinyDB

class Restaurantes:
    db = TinyDB("./db/restaurantes.json")
    restaurantes = db.table("Restaurantes")

    @classmethod
    def crear_1_restaurante(cls,nombre,decoracion,menu,comida,servicio,precio):
        restaurante = {
            "Restaurante": nombre,
            "Decoracion": decoracion,
            "Menu": menu,
            "Comida": comida,
            "Servicio": servicio,
            "Precio": precio
        }

        cls.restaurantes.insert(restaurante)

    @classmethod
    def crear_varios_restaurantes(cls, restaurantes):
        cls.restaurantes.insert_multiple(restaurantes)

    @classmethod
    def mostrar_todos_(cls):
        cls.restaurantes.all()

    