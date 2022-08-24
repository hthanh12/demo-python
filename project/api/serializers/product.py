from rest_framework import serializers
from . import *
from ..models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['member','created_at', 'updated_at', 'deleted_at', 'name', 'desc', 'status','slug','price','price_current','id']
        
    def __str__(self):
        return self.name
        
    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        field_update = ['name', 'desc', 'slug', 'price', 'price_current', 'status',]
        data_update(instance, validated_data, field_update)
        instance.save()
        return instance