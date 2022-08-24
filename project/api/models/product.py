from django.db import models
from . import *

PRODUCT_STATUSES = [
    ('ACTIVE', 'active'),
    ('BLOCKED','blocked'),
]
class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(null=True,blank=True, max_length=250)
    slug = models.CharField(max_length=250)
    price = models.FloatField()
    price_current = models.FloatField()
    status = models.CharField(choices=PRODUCT_STATUSES, default='ACTIVE', max_length=100)
    member = models.ForeignKey(Member, on_delete=models.PROTECT, default=None, null=True, blank=True)
    class Meta:
        ordering = ['created_at']