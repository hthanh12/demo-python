from django.db import models
from . import *

ORDER_STATUSES = [
    ('ACTIVE', 'active'),
    ('COMPLETED','completed'),
    ('DELETED','deleted'),
]
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    completed_at = models.DateTimeField(null=True,blank=True)
    sub_total = models.FloatField()
    total = models.FloatField()
    discount = models.ForeignKey(Discount, on_delete=models.PROTECT, default=None, null=True, blank=True)
    discount_value = models.FloatField(default=None, null=True, blank=True)
    status = models.CharField(choices=ORDER_STATUSES, default='ACTIVE', max_length=100)
    member = models.ForeignKey(Member, on_delete=models.PROTECT, default=None, null=True, blank=True)
    class Meta:
        ordering = ['created_at']