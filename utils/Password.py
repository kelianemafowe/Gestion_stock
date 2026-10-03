import bcrypt
class Password:
    
    #HashPassword:pour hashcher le mot de passe
    
    def hash_password(self,password):
        
        hashpassword_bytes=password.encode("utf-8")#transforme une chaine en binaire car bcrypt ne hash paschaine mais les binaire
        
        print(f"hashpassword_bytes={hashpassword_bytes}")
        
        hashpassword=bcrypt.hashpw(hashpassword_bytes, bcrypt.gensalt())
        
        print(f"hashpassword={hashpassword}")
        
        
        return hashpassword.decode("utf-8")

    #checkpassword
    def check_password(self,password,passwordhash):
        
        passwordbin=password.encode("utf-8")
        
        passwordhashbin=passwordhash.encode("utf-8")
        
        return bcrypt.checkpw(passwordbin,passwordhashbin)


if __name__=="__main__":
    
    password=Password()
    
    binaire=password.hash_password("keliane")
    
    print(f"passwordbin={binaire}")
    
    check=password.check_password("keliane",binaire)
    print(f"check={check}")
    
    