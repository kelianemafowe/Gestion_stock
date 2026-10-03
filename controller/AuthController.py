#Regroupe les routes d'authentification sous le préfixe/auth
from flask import Blueprint, jsonify, request
from FlaskApp.security.required.JWTRequired import jwt_required
from security.JWTService import jwt_service, JWTError

from FlaskApp.repository.ClientRepository import ClientRepository
from FlaskApp.utils.Password import Password


#pour connaitre les autres routes je dois d'abord être dans /auth
AuthConTroller=Blueprint("auth",__name__,url_prefix="/auth")

#Crée une instance du dépôt réutilisée par la route de connexion.
client_repository=ClientRepository()
password=Password()

#Accepte uniquement les reqêttes POST connexion.
@AuthConTroller.post("/login")
def login():
    #Lit le corps json sans lever d'exception si le format est incorrect
    data=request.get_json(silent=True)or {}
    #Nettoie l'email et convertt le mot de passe en chaine.
    email=str(data.get("email","")).strip()
    plain_password=str(data.get("password",""))
    
    #vérifie que les deux identifiants sont présents.
    if not email or not plain_password:
        return jsonify({"error":"email et password sont obligatoires"}),400
    
    #Recherche le client correspondant à l'email
    client=client_repository.trouver_par_email(email)
    #Refuse l'acces si le compte n'existe pas ou si le mot de passe est faux
    if not client or not password.check_password(plain_password,client["password"]):
        return jsonify({"error":"Identifiants invalides"}),401
    
    #Génère un access token court et un refresh token long
    return({
        "access_token":jwt_service.create_acces_token(client["id_client"]),
        "refresh_token":jwt_service.create_refresh_token(client["id_client"]),
        "token_type":"Bearer",
    }),200
    
@AuthConTroller.post("/refresh")
def refresh():
    #Lit le refresh token fourni dans le corp JSON.
    data=request.get_json(silent=True) or {}
    refresh_token=data.get("refresh_token","")
        
    #Refuse une requête sans à renouveler.
    if not refresh_token:
        return jsonify({"error":"refresh_token est obligatoire"}),400
    
    #Vérifie le token et effectue sa rotation à usage unique
    try:
        tokens=jwt_service.refresh(refresh_token)
        #retourne une erreur d'authentification sans exposer les détails cryptogragrie
    except JWTError as error:
        return jsonify({"error":str(error)}),401
    #retourne la nouvelle paire de tokens au client.
    return jsonify({**tokens,"token_type": "Bearer"}), 200

#Exige un refresh token valide dans le corps pour revoquer précisement cette session
@AuthConTroller.post("/logout")
@jwt_required("refresh")
def logout():
    #lit le même refresh token dans le corps pour révoquer précisement
    data=request.get_json(silent=True) or {}
    refresh_token=data.get("refresh_token","")
    #Refuse une révocation sans token explicite.
    if not refresh_token:
        return  jsonify({"error":"refresh_token est obligatoire"}),400
    
    #Ajoute le token à la liste des refresh tokens révoqués.
    try:
        jwt_service.revoke(refresh_token)
        #Signale un token invalide ou déja révoqué.
    except JWTError as error:
        return jsonify({"error":str(error)}),401
    
    #confirme la fermeture de la session renouvelable
    return jsonify({"message":"Déconnexion"}),200
    
    
    