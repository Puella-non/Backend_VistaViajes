class Destinos_model:
    def __init__(self, mysql):
        self.mysql=mysql

    def obtenerDestinos(self):
        try:        
            cursor=self.mysql.connection.cursor()
            cursor.execute("SELECT * FROM destinos")
            resultado=cursor.fetchall()
            cursor.close()
            return resultado
        
        except Exception as error:
            print("error: " + error)



