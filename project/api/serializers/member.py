from rest_framework import serializers
from . import *
from ..models import *

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [ 'id', 'username', 'fullname', 'status','created_at', 'updated_at', 'deleted_at']
        
    def __str__(self):
        return self.username
        
    def create(self, validated_data):
        """
        Create and return a new `Member` instance, given the validated data.
        """
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Member` instance, given the validated data.
        """
        field_update = ['username', 'fullname', 'status']
        data_update(instance, validated_data, field_update)
        instance.save()
        return instance
