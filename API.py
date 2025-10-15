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
        datos = Conndatabase.mostrar_todos_()
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

    @classmethod
    def encender(cls):
        cls.app.run()

api = Api()
api.encender()