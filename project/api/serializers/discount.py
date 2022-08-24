from rest_framework import serializers
from . import *
from ..models import *

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = [ 'created_at', 'updated_at', 'deleted_at', 'code', 'value','id' ]
        
    def __str__(self):
        return self.name
        
    def create(self, validated_data):
        """
        Create and return a new `Discount` instance, given the validated data.
        """
        return Discount.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Discount` instance, given the validated data.
        """
        field_update = ['code', 'value', 'status', ]
        data_update(instance, validated_data, field_update)

        instance.save()
        return instance