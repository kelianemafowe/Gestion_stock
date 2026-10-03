from abc import ABC,abstractmethod

class ClientService(ABC):
    
    #ajouter un nouveau client
    
    @abstractmethod
    def ajouter_client(self,clientEntity):
        pass
    
    @abstractmethod
    def supprimer_client(self,clientEntity):
        pass
    
    @abstractmethod
    def lister_client(self):
        pass
    
    @abstractmethod
    def modifier_client(self,clientEntity):
        pass
    
    @abstractmethod
    def rechercher_client_id(self,clientEntity):
        pass
    
    @abstractmethod
    def rechercher_client_email(self,clientEntity):
        pass
    
    @abstractmethod
    def compter_client(self):
        pass