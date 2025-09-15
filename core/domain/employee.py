class Employee:
    def __init__(
            self, 
            name, 
            department_id, 
            position_id,
            created_by,
            updated_by,
        ):
        self.name = name
        self.department_id = department_id
        self.position_id = position_id
        self.created_by = created_by
        self.updated_by = updated_by
