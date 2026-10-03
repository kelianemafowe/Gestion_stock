from service.ClientService import ClientService
from repository.ClientRepository import ClientRepository

class clientServicelmp(ClientService):
    
    clientRepository=ClientRepository()
    
    def ajouter_client(self, clientEntity):
        
        if(clientEntity.nom ==""):
            return "Le nom ne doit pas être vide"
        elif(clientEntity.email==""):
            return "L'email ne doit pas etre vide"
        elif(clientEntity.ville ==""):
            return "La ville ne doit pas être vide"
            
        elif(clientEntity.date_inscription==""):
            return "La date ne doit pas être vide"
        
        else:
            reponse=self.clientRepository.ajoute_client(clientEntity)
            
            if(reponse==-1):
                return "Erreur lors de l'ajout du client"
            
            else:
                return "Client enregistré avec succès"
    
    def rechercher_client_id(self, clientEntity):
        
        
        client=self.clientRepository.recherche_client_id(clientEntity.id_client) 
        
        if not client:
            return -1
        else:
            return client
    
    
    def supprimer_client(self, clientEntity):
        
        trouve=self.rechercher_client_id(clientEntity.id_client)
        
        if not trouve:
            return -1
        else:
            return self.clientRepository.deleteClient(clientEntity)
        
    def lister_client(self):
        
        return self.clientRepository.lister_client()
    
    def modifier_client(self,clientEntity):
        if(clientEntity.nom ==""):
            return -1
        elif(clientEntity.email==""):
            return -1
        elif(clientEntity.ville ==""):
            return -1
        elif(clientEntity.date_inscription==""):
            return -1
        else:
            modifier=self.clientRepository.updateClient(clientEntity)
            
            return modifier
        
    def compter_client(self):
            
        return self.clientRepository.countClient()
    
    def rechercher_client_email(self, clientEntity):
        
        if "" in clientEntity.email:
            return -1
        
        elif (
            "." in clientEntity.email 
            and  "@" in clientEntity.email 
            and clientEntity.email.index("@")<clientEntity.email.rindex(".")
            ):
            return self.clientRepository.updateClient(clientEntity)
        
        else:
            return -1
            
            
                
        
        
                     
            
            
    
    