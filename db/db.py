from tinydb import TinyDB

class Conndatabase:
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

    @classmethod
    def mostar_nota_media(cls):
        todos = cls.restaurantes.all()
        notas = []

        for nombre,decoracion,menu,cocina,servicio,precio in todos:
            media = float(decoracion) + float(menu) + float(cocina) + float(servicio) + float(precio)
            nota_final = media / 5 
            notas.append((nota_final, nombre))

        notas.sort(reverse=True)

        for nota,rest in notas:
            texto = f"Nombre: {rest} Nota Media: {nota}" 
        
        return texto

    @classmethod   
    def eliminar_uno(cls,nombre):
        cls.restaurantes.remove(nombre)
        
