from django.db import models
import uuid

class AuthModel(models.Model):
    id = models.AutoField(primary_key=True)
    secure_id = models.UUIDField(
        default=uuid.uuid4, editable=False,
    )
    employee_id = models.IntegerField(null=True)
    email = models.CharField()
    username = models.CharField()
    password = models.CharField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(null=True)

    class Meta:
        db_table = 'users'
        app_label = 'employee'
