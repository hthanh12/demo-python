from rest_framework import serializers
from .member import MemberSerializer
from .discount import DiscountSerializer
from .order import OrderSerializer
from .product import ProductSerializer
from .order_to_product import OrderToProductSerializer

class OrderToProductListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'id': value.id,
            'product': value.product.id,
            'amount': value.amount,
            'quantity': value.quantity
        }

data_update = lambda instance, validated_data, list: [setattr(instance, x, validated_data.get(x, getattr(instance, x))) for x in list]

def cal_total_order_current(sub_total, discount_value):
    return sub_total if discount_value is None else sub_total - ((sub_total * discount_value) / 100 )