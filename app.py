
from flask import Flask, render_template

from controller.CommandeController import CommandeControler
from controller.ClientController import ClientController


app=Flask(
    __name__,
    template_folder='view/templates',
    static_folder='view/static'
    )
app.secret_key="your secret_key"

#definition d'un blueprint

app.register_blueprint(
    ClientController.clientcontroller 
    
)
#connecte les routes du controleur à l'application principale#enregistrer le controlleur dans APP.PY
app.register_blueprint(CommandeControler.commandecontroller)


@app.route("/")
def accueil():
    
    # return """ <h1>Gestion de Stock </h1>
            
    #     <a href="/clients/"> Gestions de clients </a>
    # """
    #afficher la page d'accueil en utilisant le template accueil.html
    return render_template("commande.html")


    
    
if __name__ == "__main__":# demarer le serveur flask
        
    app.run(debug=True)#affiche les erreurs et rechargement automatique du serveurlors des modifications du