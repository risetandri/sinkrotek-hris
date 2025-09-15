from core.application.interfaces.auth import IAuthRepository
from core.domain.auth import Auth
from core.infrastructure.models.auth import AuthModel
from core.infrastructure.models.employee import EmployeeModel

class AuthRepository(IAuthRepository):
    def get_auth(self):
        return AuthModel.objects.all()
    
    def create_auth(self, auth: AuthModel):
        return AuthModel.objects.create(
            employee_id=auth.employee_id,
            email=auth.email,
            username=auth.username, 
            password=auth.password, 
            is_active=auth.is_active, 
            created_by=auth.created_by,
            updated_by=auth.updated_by,
        )
    
    def update_auth(self, secure_id, data):
        emp = AuthModel.objects.get(secure_id=secure_id)

        for key, value in data.items():
            setattr(emp, key, value)
        emp.save()

        return AuthModel.objects.all()
    
    def delete_auth(self, secure_id):
        emp = AuthModel.objects.get(secure_id=secure_id)

        emp.delete()
