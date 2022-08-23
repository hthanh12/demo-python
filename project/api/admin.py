from django.contrib import admin
from .models import Member, Product, Order, OrderToProduct, Discount

# Register your models here.
admin.site.register(Member)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderToProduct)
admin.site.register(Discount)
