from django.db import models
import uuid

class EmployeeModel(models.Model):
    id = models.AutoField(primary_key=True)
    secure_id = models.UUIDField(
        default=uuid.uuid4, editable=False,
    )
    name = models.CharField()
    department_id = models.IntegerField()
    position_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(null=True)

    class Meta:
        db_table = '"employee"."profile"'
        app_label = 'employee'
