class Auth:
    def __init__(
            self,
            employee_id,
            email,
            username, 
            password, 
            is_active, 
            created_by,
            updated_by,
        ):
        self.employee_id = employee_id
        self.email = email
        self.username = username
        self.password = password
        self.is_active = is_active
        self.created_by = created_by
        self.updated_by = updated_by
