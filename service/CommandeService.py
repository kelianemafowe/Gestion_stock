
from abc import abstractmethod


class CommandeService:
    
    #Ajouter un nouveau client(methode abstraite)
    @abstractmethod
    def ajouter_commande(self,commandeEntity):
        pass
    
    @abstractmethod
    def supprimer_commande(self,commandeEntity):
        pass
    
    @abstractmethod
    def compter_commande(self):
        pass
    
    @abstractmethod
    def lister_commande(self):
        pass
    
    @abstractmethod
    def rechercher_id(self,commandeEntity):
        pass
    
    @abstractmethod
    def modifier_commande(self,commandeEntity):
        pass
    
    
    
    