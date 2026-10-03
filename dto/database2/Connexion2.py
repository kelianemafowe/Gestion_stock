import pymysql

class Connexion2:
    
    #fonction de connexion
    def mysql_connexion(self):
        
        try:
            mysql_db=pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="gestion_stock"
            )
        
            return mysql_db
        except:
            return "Echec de connexion"
        