from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.

# Model Member
MEMBER_STATUSES = [
    ('ACTIVE', 'active'),
    ('BLOCKED','blocked'),
]
class Member(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True,blank=True)
    username = models.CharField(max_length=100)
    fullname = models.CharField(default='Fullname', blank=True, max_length=100)
    status = models.CharField(choices=MEMBER_STATUSES, default='ACTIVE', max_length=100)

    class Meta:
        ordering = ['created_at']

# Model Product
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

    class Meta:
        ordering = ['created_at']

# Model Order
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
    discount_id = models.IntegerField(null=True,blank=True)
    discount_value = models.FloatField()
    creator_id = models.IntegerField()
    status = models.CharField(choices=ORDER_STATUSES, default='ACTIVE', max_length=100)

    class Meta:
        ordering = ['created_at']

# Model OrderToProduct
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
    product_id = models.IntegerField()
    amount = models.FloatField()
    status = models.CharField(choices=ORDER_TO_PRODUCT_STATUSES, default='ACTIVE', max_length=100)

    class Meta:
        ordering = ['created_at']

# Model Discount
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
