from flask import Flask,jsonify
from flask_cors import CORS
from db.db import Conndatabase

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


app.run()

