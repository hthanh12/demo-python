from django.db import models
from . import *

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
