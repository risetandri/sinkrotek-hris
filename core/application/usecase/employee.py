from core.domain.employee import Employee
from core.domain.auth import Auth
from django.db import transaction

class EmployeeUseCase:
    def __init__(self, employee_repository, auth_repository):
        self.employee_repository = employee_repository
        self.auth_repository = auth_repository

    def get_employee(self):
        return self.employee_repository.get_employee()

    def create_employee(self, data):
        # set employee profile
        employee = Employee(
            name=data['name'],
            department_id=data['department_id'],
            position_id=data['position_id'],
            created_by=data['created_by'],
            updated_by=data['updated_by'],
        )

        result = self.employee_repository.create_employee(employee)
        
        # set employee auth table
        if 'auth' in data:
            auth = Auth(
                employee_id=result.id,
                email=data['auth']['email'],
                username=data['auth']['username'], 
                password=data['auth']['password'], 
                is_active=data['auth']['is_active'], 
                created_by=data['created_by'],
                updated_by=data['updated_by'],
            )
            
            self.auth_repository.create_auth(auth)

        return result

    def update_employee(self, secure_id, data):
        return self.employee_repository.update_employee()
    
    def delete_employee(self, secure_id):
        return self.employee_repository.delete_employee()
