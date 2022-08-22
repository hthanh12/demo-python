from rest_framework import serializers
from api.models import Member, Product, Order, OrderToProduct, Discount

data_update = lambda instance, validated_data, list: [setattr(instance, x, validated_data.get(x, getattr(instance, x))) for x in list]


# Member
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [ 'id', 'username', 'fullname', 'status','created_at', 'updated_at', 'deleted_at']
        
    def __str__(self):
        return self.name
        
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

# Product
class ProductSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['members','created_at', 'updated_at', 'deleted_at', 'name', 'desc', 'status','slug','price','price_current','id']
        
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

# Order
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
    def __str__(self):
        return self.name
        
    def create(self, validated_data):
        """
        Create and return a new `Order` instance, given the validated data.
        """
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Order` instance, given the validated data.
        """
        field_update = ['completed_at', 'sub_total', 'total', 'discount_id', 'discount_value', 'creator_id', 'status',]
        data_update(instance, validated_data, field_update)
        instance.save()
        return instance

# OrderToProduct
class OrderToProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderToProduct
        fields = '__all__'
        
    def __str__(self):
        return self.name
        
    def create(self, validated_data):
        """
        Create and return a new `OrderToProduct` instance, given the validated data.
        """
        return OrderToProduct.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `OrderToProduct` instance, given the validated data.
        """
        field_update = ['note', 'price', 'quantity', 'product_id', 'amount', 'status', ]
        data_update(instance, validated_data, field_update)

        instance.save()
        return instance

# Discount
class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'
        
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