from rest_framework import serializers
from api.models import Member, Product, Order, OrderToProduct, Discount

data_update = lambda instance, validated_data, list: [setattr(instance, x, validated_data.get(x, getattr(instance, x))) for x in list]

def cal_sum_order_current(order_id):
    return sum(list(map(lambda a : a['amount'], OrderToProduct.objects.filter(order_id=order_id).values())))

def cal_total_order_current(sub_total, discount_value):
    return sub_total if discount_value is None else sub_total - ((sub_total * discount_value) / 100 )
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

# Product
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

# Discount
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

# OrderToProduct
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
        order_sub_total = cal_sum_order_current(validated_data['order'].id) 
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

    def delete(self, instance):
        print('deletedeletedeletedelete')
        return instance

    def perform_destroy(self, instance):
        print('destroydestroydestroydestroydestroydestroydestroy')
        return instance
        
class OrderToProductListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'id': value.id,
            'product': value.product.id,
            'amount': value.amount,
            'quantity': value.quantity
        }
# Order
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
