from flask import Flask,jsonify
from flask import request
from flask_cors import CORS
from db.db import Relacional
from datetime import date

db = Relacional()

class Api:
    app = Flask(__name__)
    CORS(app)
    
    @app.route('/', methods=['GET'])
    def mostrar_nota_media():

        return jsonify([{"Nombre": nombre, "Nota": nota } for nota,nombre in datos])

    @app.route('/mostrar_puntaje', methods=['GET'])
    def mostrar_todo():
        datos = db.mostrar_restaurantes()
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/decoracion', methods=['GET'])
    def decoracion():
        datos = db.mostrar_decoracion()
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/menu', methods=['GET'])
    def menu():
        datos = db.mostrar_menu()
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/servicio', methods=['GET'])
    def servicio():
        
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/precio', methods=['GET'])
    def precio():
      
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/insertar_restaurante', methods=['POST'])
    def insertar_restaurante():
        nombre = request.form.get("nombre")
        decoracion = float(request.form.get("decoracion"))
        menu = float(request.form.get("menu"))
        comida = float(request.form.get("comida"))
        servicio = float(request.form.get("servicio"))
        precio = float(request.form.get("precio"))
        db.crear_restaurante(nombre,decoracion,menu,comida,servicio,precio)
        return jsonify ({"Nombre": nombre,
                         "Decoracion": decoracion,
                         "Menu": menu,
                         "Comida": comida,
                         "Servicio": servicio,
                         "Precio": precio
                         })
       
    
    @app.route('/nota_fecha', methods=['GET'])
    def promedio_con_fecha():

        fecha = date.today()
        fecha_string = fecha.strftime("%d-%m-%y")
        return jsonify({"Nota": nota, "Fecha": fecha_string})
    
    @app.route('/nota', methods=['GET'])
    def promedio():
        
        return jsonify({"Nota": promedio})
    
    @classmethod
    def encender(cls):
        cls.app.run(port=3000)


api = Api()
api.encender()