from datetime import datetime, timedelta , timezone
import os
import sys
from uuid import uuid4

import jwt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from security.config.JWTConfig import JWTConfig



class JWTError(Exception):
    
    pass

class JWTService:
    #refuse de démarrer si aucun secret ne protège les tokens.
    
    def __init__(self):
        
        #refuse de demarrer si aucun secret ne protège les tokens
        
        if not JWTConfig.SECRET_KEY:
            raise RuntimeError("JWT_SECRET_KEY doit être défini dans l'environnement")
        #stoke les refresh tokens révoquées pendant la durée de vie du processus
        self._revoked_refresh_tokens=set()
        
    def _create_token(self,identiy,token_type,lifetime):
        #utilise une date UTC unique pour les champs iat et exp
        now= datetime.now(timezone.utc)
        #construit les informations standard et applicatives du JW
        payload={
            "sub":str(identiy),#id du client a qui le token appartient
            "type":token_type,
            "iat":now,#date de creation du token
            "exp":now+lifetime,#date d'expiration du token
            "jti":str(uuid4()),#identifiant unique du token
        }
        #signe le token afin de detecter toute les modification
        return jwt.encode(payload,JWTConfig.SECRET_KEY,algorithm=JWTConfig.ALGORITHM)
    
    def create_acces_token(self,identity):#pour transformer un token crée a un token accéssible
        #crée un token court destiné aux appels protégées de l'API
        
        return self._create_token(
            identity,
            "access",
            timedelta(minutes=JWTConfig.ACCESS_TOKEN_EXPIRATION_SECONDE)
        )
    
    def create_refresh_token(self,identity):
        #crée un token long destiné à renouveler les tokens d'accès
        return self._create_token(
            identity,
            "refresh",
            timedelta(days=JWTConfig.REFRESH_TOKEN_EXPIRATION_DAYS)#precise la durée  de vie du token de rafraichissement en jours
            
        )
    #methode pour déchiffrer le token(avoir la bonne clé,je ne peux déchifrer un token deja modifier)
    def decode_token(self,token,expected_type=None):#pour déchiffrer le token ou jetons au même titre que JWT.io
        #verifie la signature ,l'algorithme ,l'expirattion et 
        try:
            claims=jwt.decode(
                token,
                JWTConfig.SECRET_KEY,
                algorithms=[JWTConfig.ALGORITHM],
                options={"require":["sub","type","iat","exp","jti"]},
                
            )
        #Masque les détails internes de pyJWT avec une erreur API stable/
        except jwt.PyJWTError as error:
            raise JWTError("Token invalide ou expiré") from error
        #Empêcche l'utilaisateur d'un refresh token comme token d'acces.
        if expected_type and claims.get('type') != expected_type:
            raise JWTError("Type de token invalide")
        #Refuse un refresh token déja consommé lors d'une rotation précédente:
        if claims["type"]=="refresh" and claims["jti"] in self._revoked_refresh_tokens:
            raise JWTError("Refresh token revoqué")
        #Retourne les données validées au middleware ou au contr^^oleur.
        return claims

#methode pour rafraichir un token déja inspire
    def refresh(self,refresh_token):
        #valide l'ancien refresh token avant d'en émettre un nouveau
        claims=self.decode_token(refresh_token,expected_type="refresh")
        #revoque l'ancien  token pour enpêcher sa reutilisation.
        self._revoked_refresh_tokens.add(claims["jti"])
        #Reutilise l'identité origine pour la nouvelle paire de toke,
        identity=claims["sub"]
        #retourne une paire entièrement renouvelée
        return{
            "access_token":self.create_acces_token(identity),
            "refresh_token":self.create_refresh_token(identity),
        }
    
    #Arrêter la capacité d'un token dêtre accessible(rendre unitile)
    def revoke(self,token):
        #verifie que le token à revoquer est bien un refresh token valide
        claims=self.decode_token(token,expected_type="refresh")
        #Ajoute son identifiant à la liste des tokens inutilisable
        self._revoked_refresh_tokens.add(claims["jti"])
        

jwt_service=JWTService()
access_token=jwt_service.create_acces_token(1)
print("Access Token:",access_token)
    
    # refresh_token=jwt_service.create_refresh_token(1)
    # print("Refresh Token:",refresh_token)
    
    # decode_token=jwt_service.decode_token(access_token,"access")#prnd le token et le type de token
    # print("decode_token:",decode_token)
    
    # rafraichir_token=jwt_service.refresh(refresh_token)
    # print("rafraichir:",rafraichir_token)
    
    # refresh_token=jwt_service.create_refresh_token(1)
    # print(jwt_service.revoke(refresh_token))
    
        