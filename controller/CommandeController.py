from flask import Blueprint, redirect, render_template, request, url_for, flash

from entities.CommandeEntity import Commande
from servicelmp.CommandeServiceImp import CommandeServiceImp


class CommandeControler:

    commandecontroller = Blueprint(
        "commande",
        __name__,
        url_prefix="/commande"
    )

    commandeservice = CommandeServiceImp()

    @commandecontroller.route("/ajouter/commande", methods=["POST"])
    def ajouter_commande():
        try:
            if request.is_json:
                donnees = request.get_json()
                commandes = donnees.get("commande", [])

                for commande in commandes:
                    client_entity = Commande(
                        None,
                        str(commande.get("quantite", "")).strip(),
                        str(commande.get("prix_unitaire", "")).strip(),
                        str(commande.get("id_client", "")).strip()
                    )
                    resultat = CommandeControler.commandeservice.ajouter_commande(client_entity)

                    if resultat == -1:
                        flash("Erreur lors de l'ajout d'une commande", "danger")
                        break
                    else:
                        flash("Commandes enregistrées avec succès", "success")
            else:
                client_entity = Commande(
                    None,
                    request.form.get("quantite", "").strip(),
                    request.form.get("prix_unitaire", "").strip(),
                    request.form.get("id_client", "").strip()
                )

                resultat = CommandeControler.commandeservice.ajouter_commande(client_entity)
                if resultat == -1:
                    flash("Erreur lors de l'ajout d'une commande", "danger")
                else:
                    flash("L'ajout d'une commande a été effectué avec succès", "success")

        except Exception as erreur:
            print("Erreur :", erreur)
            flash("Une erreur s'est produite", "danger")

        return redirect(url_for("commande.liste_commandes"))

    @commandecontroller.route("/liste/commande", methods=["GET"])
    def liste_commandes():
        commandes = CommandeControler.commandeservice.liste_commande()
        if commandes == -1:
            flash("Impossible de se connecter à la base de données")
            commandes = []

        return render_template("liste_commande.html", commandes=commandes)

    @commandecontroller.route("/nouvelle", methods=["GET"])
    def nouvelle_commande():
        return render_template("commande.html")