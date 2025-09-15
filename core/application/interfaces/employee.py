from abc import ABC, abstractmethod
from core.domain.employee import Employee

class IEmployeeRepository(ABC):
    @abstractmethod
    def get_employee(self):
        pass
    
    @abstractmethod
    def create_employee(self, employee: Employee):
        pass
    
    @abstractmethod
    def update_employee(self, secure_id, employee: Employee):
        pass
    
    @abstractmethod
    def delete_employee(self, secure_id):
        pass
