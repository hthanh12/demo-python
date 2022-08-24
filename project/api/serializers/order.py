from rest_framework import serializers
from . import *
from ..models import *

class OrderSerializer(serializers.ModelSerializer):
    # products = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field=['amount','id']
    #  )
    # products = OrderToProductSerializer(many=True, read_only=True)
    products = OrderToProductListingField(many=True, read_only=True)


    class Meta:
        model = Order
        fields = [  'id', 'member','discount', 'created_at', 'updated_at', 'deleted_at', 'completed_at', 'sub_total', 'total', 'discount_value', 'products']

    def __str__(self):
        return self.total
        
    def create(self, validated_data):
        """
        Create and return a new `Order` instance, given the validated data.
        """
        # print('validated_data',validated_data)
        # print('validated_data',validated_data['discount'].id)
        discount_id = validated_data.get('discount').id if validated_data.get('discount') else None
        discount = {}

        if(discount_id is not None):
            discount = Discount.objects.get(pk=discount_id)

        validated_data = { **validated_data, "discount_value": discount.get('value', None)}
        print('0000000000000000000000000000000000000000000000000000000000000000000000000000')
        print(validated_data)
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Order` instance, given the validated data.
        """
        field_update = ['completed_at', 'sub_total', 'total', 'discount', 'discount_value', 'status']
        data_update(instance, validated_data, field_update)
        
        instance.save()
        return instance