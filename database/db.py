from flask_mysqldb import MySQL
    
def init_database(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'Puella_non1987'
    app.config['MYSQL_DB'] = 'vistaViajes'
    return MySQL(app)
