from flask import Flask
from flask_cors import CORS
from database.db import init_database 
from controllers.destinos_controller import init_destinos_controller
from controllers.viajes_controller import init_viajes_controller
from routes.routes import routes 

app = Flask(__name__)
CORS(app)

app.register_blueprint(routes)
mySQL = init_database(app)

init_destinos_controller(app, mySQL)
init_viajes_controller(app, mySQL)

if __name__ == "__main__":
    app.run(debug=True, port=3000)

