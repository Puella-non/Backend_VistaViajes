from flask import Blueprint
from controllers.destinos_controller import obtenerDestinos
from controllers.viajes_controller import obtenerViajes

routes=Blueprint("routes", __name__)

routes.route("/obtenerDestinos", methods=["GET"])(obtenerDestinos)
routes.route("/obtenerViajes", methods=["GET"])(obtenerViajes)