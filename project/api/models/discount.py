from django.db import models
from . import *

DISCOUNT_STATUSES = [
    ('ACTIVE', 'active'),
    ('BLOCKED','blocked'),
]
class Discount(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    code = models.CharField(max_length=100)
    value = models.FloatField()
    status = models.CharField(choices=DISCOUNT_STATUSES, default='ACTIVE', max_length=100)

    class Meta:
        ordering = ['created_at']