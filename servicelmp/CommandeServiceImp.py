from servicelmp.ClientServiceImple import clientServicelmp
from service.CommandeService import CommandeService
from repository.CommandeRepository import CommandeRepository

class CommandeServiceImp(CommandeService):
    
    commandeRepository=CommandeRepository()
    
    def ajouter_commande(self, commandeEntity):
        #pour ajouter une nouvelle commande il faut client soit déja dans bd 
        #recherche le client à partir de son id dans la table commande
        
        
        
        # client = clientServicelmp.rechercher_client_id(commandeEntity)
        
        # if not client :#on verifie s'il est une instance de client sinon retourner -1 
        #     return -1
        
        if commandeEntity.quantite=="":
            return -1
        elif commandeEntity.prix_unitaire=="":
            return -1
        else:
            commande=self.commandeRepository.ajouter_commande(commandeEntity)
            if not commande:#pour verifier si j'ajout a reussir
                return -1
            else:
                return commande
    
    #methode pour rechercher une commande
    def rechercher_id(self, commandeEntity):
        if commandeEntity.id_client=="":
            return -1
        else:
            trouve=self.commandeRepository.rechercher_commande(commandeEntity)
    
    #methode pour supprimer 
    def supprimer_commande(self, commandeEntity):
        
        commande=self.rechercher_id(commandeEntity)
        
        if not commande:
            return -1
        else:
            return commande
    
    #compter le nombre de commande
    def compter_commande(self):
        return self.commandeRepository.compter_commande()
        
    #methode pour lister les commandes
    def liste_commande(self):
        return self.commandeRepository.lister_commande()
    
    #methode pour modifier une commande
    def modifier_commande(self,commandeEntity):
        if commandeEntity.id_client=="":
            return -1
        elif commandeEntity.quantite=="":
            return -1
        elif commandeEntity.prix_unitaire=="":
            return -1
        else:
            return self.commandeRepository.modifier_commande
    
        
        
    