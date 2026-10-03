from database2.Connexion2 import Connexion2


class CommandeRepository:

    def ajouter_commande(self, commandeEntity):
        try:
            connexion = Connexion2()
            mysql_db = connexion.mysql_connexion()
            mycurseur = mysql_db.cursor()

            sql = "INSERT INTO commande (quantite, prix_unitaire, id_client) VALUES (%s, %s, %s)"
            valeur = (commandeEntity.quantite, commandeEntity.prix_unitaire, commandeEntity.id_client)

            mycurseur.execute(sql, valeur)
            mysql_db.commit()

            nombre_lignes = mycurseur.rowcount
            mysql_db.close()
            return nombre_lignes
        except Exception as e:
            print("Erreur ajout commande :", e)
            return -1

    def supprimer_commande(self, commandeEntity):
        try:
            connexion = Connexion2()
            mysql_db = connexion.mysql_connexion()
            mycurseur = mysql_db.cursor()

            sql = "DELETE FROM commande WHERE id_commande=%s"
            valeur = (commandeEntity.id_commande,)

            mycurseur.execute(sql, valeur)
            mysql_db.commit()
            mysql_db.close()

            return mycurseur.rowcount
        except Exception as e:
            print("Erreur suppression commande :", e)
            return -1

    def compter_commande(self):
        try:
            connexion = Connexion2()
            mysql_db = connexion.mysql_connexion()
            mycurseur = mysql_db.cursor()

            sql = "SELECT COUNT(*) FROM commande"
            mycurseur.execute(sql)

            nombre_commande = mycurseur.fetchone()
            mysql_db.close()

            return nombre_commande
        except Exception as e:
            print("Erreur count commande :", e)
            return -1

    def lister_commande(self):
        try:
            connexion = Connexion2()
            mysql_db = connexion.mysql_connexion()
            mycurseur = mysql_db.cursor()

            sql = "SELECT * FROM commande"
            mycurseur.execute(sql)

            liste_commande = mycurseur.fetchall()
            mysql_db.close()

            return liste_commande
        except Exception as e:
            print("Erreur liste commande :", e)
            return -1

    def modifier_commande(self, commandeEntity):
        try:
            connexion = Connexion2()
            mysql_db = connexion.mysql_connexion()
            mycurseur = mysql_db.cursor()

            sql = "UPDATE commande SET quantite=%s, prix_unitaire=%s, id_client=%s WHERE id_commande=%s"
            valeur = (commandeEntity.quantite, commandeEntity.prix_unitaire, commandeEntity.id_client, commandeEntity.id_commande)

            mycurseur.execute(sql, valeur)
            mysql_db.commit()
            mysql_db.close()

            return mycurseur.rowcount
        except Exception as e:
            print("Erreur modif commande :", e)
            return -1

    def rechercher_commande(self, commandeEntity):
        try:
            connexion = Connexion2()
            mysql_db = connexion.mysql_connexion()
            mycurseur = mysql_db.cursor()

            sql = "SELECT * FROM commande WHERE id_commande=%s"
            valeur = (commandeEntity.id_commande,)

            mycurseur.execute(sql, valeur)
            trouve = mycurseur.fetchone()
            mysql_db.close()

            return trouve
        except Exception as e:
            print("Erreur recherche commande :", e)
            return -1