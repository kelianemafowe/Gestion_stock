import os

from dotenv import load_dotenv


BASE_DIR=os.path.abspath(os.path.join(os.path.dirname(__file__),"..",".."))#permet ))

load_dotenv(dotenv_path=os.path.join(BASE_DIR,".env"))


class JWTConfig:#information essentielle pour la création et la validation des tokens jwt
    #récupère la clé secrète à partir des var
    SECRET_KEY=os.getenv("SECRET_KEY")
    #algothme de s
    ALGORITHM=os.getenv("ALGORITH","HS256")
    
    ACCESS_TOKEN_EXPIRATION_SECONDE=int(os.getenv("Access_TOken_EXPIRE_SECONDES","15"))
    
    REFRESH_TOKEN_EXPIRATION_DAYS=int(os.getenv("REFRESH_TOKEN_EXPIRATION_DAYS","30"))
    
    
    
    
    

    