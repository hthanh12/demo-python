from django.db import models
from . import *

ORDER_TO_PRODUCT_STATUSES = [
    ('ACTIVE', 'active'),
    ('DELETED','deleted'),
]
class OrderToProduct(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    note = models.CharField(max_length=250)
    price = models.FloatField()
    quantity = models.IntegerField()
    amount = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    class Meta:
        ordering = ['created_at']