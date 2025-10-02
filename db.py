from tinydb import TinyDB

class Restaurantes:
    db = TinyDB("./db/restaurantes.json")
    restaurantes = db.table("Restaurantes")

    def crear_1_restaurante(self,nombre,decoracion,menu,comida,servicio,precio):
        restaurante = {
            "Restaurante": nombre,
            "Decoracion": decoracion,
            "Menu": menu,
            "Comida": comida,
            "Servicio": servicio,
            "Precio": precio
        }

        self.__class__.restaurantes.insert(restaurante)

    def crear_varios_restaurantes(self, restaurantes):
        self.__class__.restaurantes.insert_multiple(restaurantes)

    def mostrar_todos_(self):
        self.__class__.restaurantes.all()

    def mostar_nota_media(self):
        todos = self.__class__.restaurantes.all()
        notas = []

        for nombre,decoracion,menu,cocina,servicio,precio in todos:
            media = float(decoracion) + float(menu) + float(cocina) + float(servicio) + float(precio)
            nota_final = media / 5 
            notas.append((nota_final, nombre))

        notas.sort(reverse=True)

        for nota,rest in notas:
            texto = f"Nombre: {rest} Nota Media: {nota}" 
        
        return texto
            
    def eliminar_uno(self,nombre):
        self.__class__.restaurantes.remove(nombre)
        
