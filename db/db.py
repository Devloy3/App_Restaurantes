import sqlite3

class NoRelacional:
    conn = sqlite3.connect("./db/restaurantes.db")
    cursor = conn.cursor()
    
    @classmethod
    def crear_restaurante(cls,nombre,decoracion,menu,comida,servicio,precio):
        cls.cursor.execute("INSERT INTO restaurantes(Restaurante,Decoracion,Menu,Comida,Servicio,Precio) VALUES (?,?,?,?,?,?)",(nombre,decoracion,menu,comida,servicio,precio))
        cls.conn.commit()
    
    @classmethod
    def mostrar_todos(cls):
        cls.cursor.execute("SELECT * FROM restaurantes;")
        todo = cls.cursor.fetchall()
        return todo
    
    @classmethod
    def ordenar_por_decoracion(cls):
       cls.cursor.execute("SELECT * FROM restaurantes ORDER BY Decoracion;")
       todo = cls.cursor.fetchall()
       return todo
   
    @classmethod
    def ordenar_por_menu(cls):
        restaurante = []
        todo = cls.restaurantes.all()
        for division in todo:
            nombre = division["Restaurante"]
            decoracion = division["Decoracion"]
            menu = division["Menu"]
            cocina = division["Comida"]
            servicio = division["Servicio"]
            precio = division["Precio"]
            restaurante.append((nombre,float(decoracion),float(menu),float(cocina),float(servicio),float(precio)))
        
        restaurante.sort(key=lambda x:x[2], reverse=True)

        return restaurante
    
    @classmethod
    def ordenar_por_cocina(cls):
        restaurante = []
        todo = cls.restaurantes.all()
        for division in todo:
            nombre = division["Restaurante"]
            decoracion = division["Decoracion"]
            menu = division["Menu"]
            cocina = division["Comida"]
            servicio = division["Servicio"]
            precio = division["Precio"]
            restaurante.append((nombre,float(decoracion),float(menu),float(cocina),float(servicio),float(precio)))
        
        restaurante.sort(key=lambda x:x[3], reverse=True)

        return restaurante
    
    @classmethod
    def ordenar_por_servicio(cls):
        restaurante = []
        todo = cls.restaurantes.all()
        for division in todo:
            nombre = division["Restaurante"]
            decoracion = division["Decoracion"]
            menu = division["Menu"]
            cocina = division["Comida"]
            servicio = division["Servicio"]
            precio = division["Precio"]
            restaurante.append((nombre,float(decoracion),float(menu),float(cocina),float(servicio),float(precio)))
        
        restaurante.sort(key=lambda x:x[4], reverse=True)

        return restaurante

    @classmethod
    def ordenar_por_precio(cls):
        restaurante = []
        todo = cls.restaurantes.all()
        for division in todo:
            nombre = division["Restaurante"]
            decoracion = division["Decoracion"]
            menu = division["Menu"]
            cocina = division["Comida"]
            servicio = division["Servicio"]
            precio = division["Precio"]
            restaurante.append((nombre,float(decoracion),float(menu),float(cocina),float(servicio),float(precio)))
        
        restaurante.sort(key=lambda x:x[5], reverse=True)

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
    
    
    @classmethod
    def mostar_el_promedio_total(cls):
        todo = cls.restaurantes.all()
        largura = len(todo)
        notas = []

        for division in todo:
            decoracion = division["Decoracion"]
            menu = division["Menu"]
            cocina = division["Comida"]
            servicio = division["Servicio"]
            precio = division["Precio"]
            media = float(decoracion) + float(menu) + float(cocina) + float(servicio) + float(precio)
            nota_final = media / 5 
            redondeo = round(nota_final, 1)
            notas.append(redondeo)
        
        total = sum(notas) / largura
        redondeo_final = round(total,1)
        
        return redondeo_final
    

     

            


        
        
