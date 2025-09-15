from django.db import models
import uuid

class SalaryModel(models.Model):
    id = models.IntegerField()
    secure_id = models.UUIDField(
        default=uuid.uuid4, editable=False,
    )
    amount = models.FloatField()
    allowance = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField()
    
    class Meta:
        db_table = '"employee"."salary"'
        app_label = 'employee'