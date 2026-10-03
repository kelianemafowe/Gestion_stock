from flask import Blueprint, flash, redirect, render_template, request, url_for


from entities.ClientEntity import ClientEntity
from servicelmp.ClientServiceImple import clientServicelmp


class ClientController:
    
    clientcontroller=Blueprint(#permet d'organiser les routes flask par fonctionnalité,ici les routes sont liées a la gestion des clients
        "client",
        __name__,
        url_prefix="/client"
    )
    
    clientservice=clientServicelmp()
    
    #route pour ajouter un client,la route est /ajouter/client et la méthode est POST pourenvoyer les données du client à ajouter
    @clientcontroller.route("/ajouter/client",methods=["POST"])
    def ajouter_client():
        try:
            if request.is_json:
                donnees=request.get_json()
                clients=donnees.get("client",[])
                
                for client in clients:
                    #crée un objet client à partir des données reçues et l'ajoute à la base de données
                    client_entity=ClientEntity(
                    None,
                    str(client.get("nom","")).strip(),#recupère le nom str() transforme en string
                    str(client.get("email","")).strip(),
                    str(client.get("ville","")).strip(),
                    str(client.get("date_inscription","")).strip()
                    )
                    #enregistre le client dans la base de données en utilisant le service client
                    resultat=ClientController.clientservice.ajouter_client(client_entity)
                    
                    if resultat==-1:#verifie le resultat si le service renvoi -1 ,une erreur est survenue
                        flash("Erreur lors de l'ajout d'un client","danger")
                        break
                    else:
                        flash("Clients enrégistrés avec succès","success")
            else:#cas ou si la requête n'est pas sur format json,on suppose que c'est un formulaire html
                #cree un objet client à partir des données du formulaire et l'ajoute à la bd
                client_entity=ClientEntity(#
                    None,
                    request.form.get("nom","").strip(),
                    request.form.get("email","").strip(),
                    request.form.get("ville","").strip(),
                    request.form.get("date_inscription","").strip()
                )
                
                resultat=ClientController.clientservice.ajouter_client(client_entity)
                if resultat==-1:
                    flash("Erreur lors de l'enrégistrement du client","danger")
                else:
                    flash("Client enrégistrer avec succès","success")
        
        except Exception as erreur:
            print(erreur)
            flash("Une erreur  s'est produite","danger")
        return redirect(url_for("client.liste_clients"))#redirection vers la route liste clients après l'ajout du client
    
    #get pour dire que l'utilisateur veut voirs la liste des clients,la route est/liste/clients
    @clientcontroller.route("/liste/clients", methods=["GET"])
    def liste_clients():
        clients = ClientController.clientservice.lister_client()
        #Verification si la liste des clients est vide ou si une erreur s'est produite lors de la 
        if clients == -1:
            flash("Impossible de se connecter à la base de données", "danger")
            clients = []#Remplace le resultat par une liste vide afin d'éviter les 
            #erreurs lors de l'affichage de la liste des clients

        return render_template(
            "liste_client.html",
            clients=clients
        )                   
    
   