from core.application.interfaces.employee import IEmployeeRepository
from core.domain.employee import Employee
from core.infrastructure.models.employee import EmployeeModel

class EmployeeRepository(IEmployeeRepository):
    def get_employee(self):
        return EmployeeModel.objects.all()
    
    def create_employee(self, employee: Employee):
        return EmployeeModel.objects.create(
            name=employee.name, 
            department_id=employee.department_id, 
            position_id=employee.position_id,
            created_by=employee.created_by,
            updated_by=employee.updated_by,
        )
    
    def update_employee(self, secure_id, data):
        emp = EmployeeModel.objects.get(secure_id=secure_id)

        for key, value in data.items():
            setattr(emp, key, value)
        emp.save()

        return emp
    
    def delete_employee(self, secure_id):
        emp = EmployeeModel.objects.get(secure_id=secure_id)

        emp.delete()
