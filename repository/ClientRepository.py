from database.Connexion import Connexion

class ClientRepository:
    
    #ajouter un nouveau client
    
    def ajoute_client(self,clientEntity):
        
        try:
            
            connexion=Connexion()
            
            #se connecter
            
            mysql_db=connexion.mysql_connexion()
            
            #creer le curseur
            
            mycurseur=mysql_db.cursor()
            
            #requette sql
            
            sql="INSERT INTO client(nom,email,ville,date_inscription) VALUES(%s,%s,%s,%s)"
            
            value=(clientEntity.nom,clientEntity.email,clientEntity.ville,clientEntity.date_inscription)
            
            mycurseur.execute(sql,value)
            
            #commit
            mysql_db.commit()
            mysql_db.close()
            
            return mycurseur.rowcount
        
        except:
            
            return -1
        
    #methode pour supprimer
    
    def lister_client(self):
        
        try:
            
            connexion=Connexion()
            
            mysql_db=connexion.mysql_connexion()
            
            mycurseur=mysql_db.cursor()
            
            #requette pour afficher
            
            sql="SELECT * FROM  client"
            
            mycurseur.execute(sql)

            liste_client=mycurseur.fetchall()
            mysql_db.close()
            
            return liste_client
        except:
            
            return -1
    
    # methode pour compter le  nombre de client
    
    def countClient(self):
        
        try:
        
            connexion=Connexion()
            
            #se connecter
            
            mysql_db=connexion.mysql_connexion()
            
            #creer le curseur
            
            mycurseur=mysql_db.cursor()
            
            #requete sql
            
            sql="SELECT COUNT(*) FROM  client"
            
            mycurseur.execute(sql)
            
            nombre_client=mycurseur.fetchone()
            
            mysql_db.close()
            
            return nombre_client

        except:
            return -1
        
    #Supprimer un client
        
    def deleteClient(self,clientEntity):
        
        try:
            
            connexion=Connexion()
                    
            #se connecter
            
            mysql_db=connexion.mysql_connexion()
            
            mycurseur=mysql_db.cursor()
            
            sql="DELETE FROM client WHERE id_client=%s"
            value=(clientEntity.id_client)
            
            mycurseur.execute(sql,value)
            
            mysql_db.commit()
            
            mysql_db.close()
            
            return mycurseur.rowcount()
        
        except:
            
            return -1
        
    #methode pour modifier
    
    def updateClient(self,clientEntity):
        
        try:
            
            connexion=Connexion()
            
            #se connecter
            
            connexion=Connexion()
            
            mysql_db=connexion.mysql_connexion()
            
            curseur=mysql_db.cursor()
            
            sql="UPDATE client SET nom=%s,email=%s,ville=%s,date_inscription=%s WHERE id_client=%s"
            
            valeur=(clientEntity.nom,clientEntity.email,clientEntity.ville,clientEntity.date_inscription,clientEntity.id_client)
            
            curseur.execute(sql,valeur)
            
            #commit
            
            mysql_db.commit()
            mysql_db.close()
            
            return curseur.rowcount()
        
        except:
            return -1
    
    #recherchez le client à partir de son id
    def recherche_client_id(self,clientEntity):
        try:
            connexion=Connexion()
            #se connecter
            mysql_db=connexion.mysql_connexion()
            
            #creation du curseur
            my_cursor=mysql_db.cursor()
            #requêtte
            sql="SELECT * FROM client WHERE id_client=%s"
            valeur=clientEntity.id_client
            
            my_cursor.execute(sql,valeur)
            
            trouve=my_cursor.fetchone()
            
            mysql_db.close()
            
            return trouve
        except:
            return -1
    
    def recherche_client_email(self,clientEntity):
        try:
            #instance
            connexion=Connexion()
            #se connecter
            mysql_db=connexion.mysql_connexion()
            mycurseur=mysql_db.cursor()
            #requêtte
            sql="SELECT * FROM client WHERE email=%s"
            
            valeur=clientEntity.email
            
            mycurseur.execute(sql,valeur)
            
            trouve=mycurseur.fetchone()
            
            mysql_db.close()
            
            return trouve
        
        except:
            return -1
        
        
    def trouver_par_email(self,email):
        
        try:
        
            connexion=Connexion()
            
            mysql_db=connexion.mysql_connexion()
            
            mysql_curseur=mysql_db.cursor()
            
            sql="SELECT * FROM client WHERE email=%s"
            valeur=email
            
            mysql_curseur.execute(sql,valeur)
            
            trouve=mysql_curseur.fetchone()
            
            mysql_db.close()
            
            return trouve
        except:
            return -1
                
                            
                
        
            
                
                
                
            
                
                
            
                