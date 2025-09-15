from abc import ABC, abstractmethod
from core.domain.auth import Auth

class IAuthRepository(ABC):
    @abstractmethod
    def get_auth(self):
        pass
    
    @abstractmethod
    def create_auth(self, auth: Auth):
        pass
    
    @abstractmethod
    def update_auth(self, secure_id, auth: Auth):
        pass
    
    @abstractmethod
    def delete_auth(self, secure_id):
        pass
