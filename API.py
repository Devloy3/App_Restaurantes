from flask import Flask,jsonify
from flask import request
from flask_cors import CORS
from db.db import NoRelacional
from datetime import date

class Api:
    app = Flask(__name__)
    CORS(app)
    
    @app.route('/', methods=['GET'])
    def mostrar_nota_media():
        datos = NoRelacional.mostar_nota_media()
        return jsonify([{"Nombre": nombre, "Nota": nota } for nota,nombre in datos])

    @app.route('/mostrar_puntaje', methods=['GET'])
    def mostrar_todo():
        datos = NoRelacional.mostrar_todos()
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/decoracion', methods=['GET'])
    def decoracion():
        datos = NoRelacional.ordenar_por_decoracion()
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/menu', methods=['GET'])
    def menu():
        datos = NoRelacional.ordenar_por_menu()
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/servicio', methods=['GET'])
    def servicio():
        datos = NoRelacional.ordenar_por_servicio()
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/precio', methods=['GET'])
    def precio():
        datos = NoRelacional.ordenar_por_precio()
        return jsonify([{"Nombre": nombre, "Decoracion": decoracion, "Menu": menu, "Cocina": cocina, "Servicio": servicio, "Precio": precio} for nombre,decoracion,menu,cocina,servicio,precio in datos])
    
    @app.route('/insertar_restaurante', methods=['POST'])
    def insertar_restaurante():
        nombre = request.form.get("nombre")
        decoracion = request.form["decoracion"]
        menu = request.form["menu"]
        comida = request.form["comida"]
        servicio = request.form["servicio"]
        precio = request.form["precio"]
        NoRelacional.crear_1_restaurante(nombre,decoracion,menu,comida,servicio,precio)
        return jsonify ({"Datos": "Datos insertados correctamente"})
    
    @app.route('/nota_fecha', methods=['GET'])
    def promedio_con_fecha():
        nota = NoRelacional.mostar_el_promedio_total()
        fecha = date.today()
        fecha_string = fecha.strftime("%d-%m-%y")
        return jsonify({"Nota": nota, "Fecha": fecha_string})
    
    @app.route('/nota', methods=['GET'])
    def promedio():
        promedio = NoRelacional.mostar_el_promedio_total()
        return jsonify({"Nota": promedio})
    
    @classmethod
    def encender(cls):
        cls.app.run(port=3000)


api = Api()
api.encender()