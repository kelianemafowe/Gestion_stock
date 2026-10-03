from functools import wraps
from security.JWTService import jwt_service, JWTError

from flask import g, jsonify, request


def jwt_required(token_type="access"):
    #Reçoit le type de token autorisé par la route protégée.
    def decorator(view):
        #Construit le wrapper exécuté avant la fonction de route.
        @wraps(view)
        def wrapped(*args,**kwargs):
            #Récupère l'entête authorization envoyé par le client
            authorization=request.headers.get("authorization","")
            #sépare le schema Bearer de la valeur du token
            scheme,token=authorization.partition("")
            
            #Refuse les requêtes qui ne suivent pas le format Bearer.
            if scheme.lower()!="bearer" or not token:
                return jsonify({"error":"Bearer token requis"})
            #Valide le JWT et rend ses et rend ses claims disponibles dans g.current
            try:
                g.current_user=jwt_service.decode_token(token,expected_type=token_type)
            #Transforme toute erreur  JWT en réponse HTTP 401.
            except JWTError as error:
                return jsonify({"error":str(error)}),401
            
            #Continue vers la route uniquement après validation
            return view(*args,**kwargs)
        #Retourne la route enrichie par la protection JWT
        return wrapped
    #Retourne le décorateur configuré
    return decorator
                
                