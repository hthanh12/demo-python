from rest_framework import serializers
from . import *
from ..models import *

class OrderToProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderToProduct
        fields = [ 'id','created_at', 'updated_at', 'deleted_at', 'note', 'price', 'quantity', 'amount',  'order','product']
        
    def __str__(self):
        return self.name
        
    def create(self, validated_data):
        """
        Create and return a new `OrderToProduct` instance, given the validated data.
        """
        # order_sub_total = cal_sum_order_current(validated_data['order'].id) 
        order_sub_total = 0
        order = validated_data['order']
        amount = validated_data['product'].price_current * validated_data['quantity']
        order_sub_total += amount

        order_total = cal_total_order_current(order_sub_total, order.discount_value)
        order.sub_total = order_sub_total
        order.total = order_total
        order.save()

        validated_data = { **validated_data, "amount": amount}

        return OrderToProduct.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `OrderToProduct` instance, given the validated data.
        """
        field_update = ['note', 'price', 'quantity', 'product_id', 'amount', 'status', ]
        data_update(instance, validated_data, field_update)

        instance.save()
        return instance
