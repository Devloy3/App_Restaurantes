from flask import Flask,jsonify
from flask import request
from flask_cors import CORS
from db.db import Conndatabase

class Api:
    app = Flask(__name__)
    CORS(app)
    
    @app.route('/', methods=['GET'])
    def mostrar_nota_media():
        datos = Conndatabase.mostar_nota_media()
        return jsonify([{"Nombre": nombre, "Nota": nota } for nota,nombre in datos])

    @app.route('/mostrar_puntaje', methods=['GET'])
    def mostrar_todo():
        datos = Conndatabase.mostrar_todos()
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/decoracion', methods=['GET'])
    def decoracion():
        datos = Conndatabase.ordenar_por_decoracion()
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/menu', methods=['GET'])
    def menu():
        datos = Conndatabase.ordenar_por_menu()
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/servicio', methods=['GET'])
    def servicio():
        datos = Conndatabase.ordenar_por_servicio()
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/precio', methods=['GET'])
    def precio():
        datos = Conndatabase.ordenar_por_precio()
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/insertar_restaurante', methods=['POST'])
    def insertar_restaurante():
        nombre = request.form.get("nombre")
        decoracion = request.form["decoracion"]
        menu = request.form["menu"]
        comida = request.form["comida"]
        servicio = request.form["servicio"]
        precio = request.form["precio"]
        Conndatabase.crear_1_restaurante(nombre,decoracion,menu,comida,servicio,precio)
        return jsonify ({"Datos": "Datos insertados correctamente"})
    
    @app.route('/mostrar_promedio_total', methods=['GET'])
    def promedio_total():
        promedio = Conndatabase.mostar_el_promedio_total()
        return jsonify({"Promedio Total": promedio})
    
    def encender(cls):
        cls.app.run()

api = Api()
api.encender()