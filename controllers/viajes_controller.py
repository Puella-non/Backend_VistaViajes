from flask import request, jsonify, Blueprint
from models.viajes_model import Viajes_model

viajes_controller=Blueprint("viajes_controller", __name__)

def init_viajes_controller(app, mySQL):
    global Viajes_model
    Viajes_model=Viajes_model(mySQL)
    app.register_blueprint(viajes_controller)

def obtenerViajes():
    try:
        return jsonify(Viajes_model.obtenerViajes())
    except Exception as error:
        print("error: " + str(error))

