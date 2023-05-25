from flask import request, jsonify, Blueprint
from models.destinos_model import Destinos_model

destinos_controller=Blueprint("destinos_controller", __name__)

def init_destinos_controller(app, mySQL):
    global Destinos_model
    Destinos_model=Destinos_model(mySQL)
    app.register_blueprint(destinos_controller)

def obtenerDestinos():
    try:
        return jsonify(Destinos_model.obtenerDestinos())
    except Exception as error:
        print("error: " + str(error))

