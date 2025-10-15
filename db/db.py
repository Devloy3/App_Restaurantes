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
        restaurante = []
        todo = cls.restaurantes.all()
        for division in todo:
            nombre = division["Restaurante"]
            decoracion = division["Decoracion"]
            menu = division["Menu"]
            cocina = division["Comida"]
            servicio = division["Servicio"]
            precio = division["Precio"]
            restaurante.append((nombre,decoracion,menu,cocina,servicio,precio))

        return restaurante
            

    @classmethod
    def mostar_nota_media(cls):
        todo = cls.restaurantes.all()
        notas = []

        for division in todo:
            nombre = division["Restaurante"]
            decoracion = division["Decoracion"]
            menu = division["Menu"]
            cocina = division["Comida"]
            servicio = division["Servicio"]
            precio = division["Precio"]
            media = float(decoracion) + float(menu) + float(cocina) + float(servicio) + float(precio)
            nota_final = media / 5 
            redondeo = round(nota_final, 1)
            notas.append((redondeo, nombre))

        notas.sort(reverse=True)
        
        return notas
        
