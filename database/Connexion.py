import os
from dotenv import load_dotenv
import pymysql

#charger le  .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

class Connexion:
    
    #se connecter a la base de donnée
    
    def mysql_connexion(self):
        
        try:
            mysql_db=pymysql.connect(
                
                host=os.getenv("DB_HOST"), #permet de recuperer la valeur de la variable d'environnement DB_HOST
                user=os.getenv("DB_user"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
                
            )
            
            return mysql_db
        except:
            
            return "Echec de connexion"
        