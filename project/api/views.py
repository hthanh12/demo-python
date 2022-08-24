# Create your views here.
from django.http import Http404
from distutils.log import error
from api.models import *
from api.serializers import *
from rest_framework import mixins
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Check health
class Pong(APIView):
    def get(self, request):
        return Response('pong')
# Route Member
class MemberList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView,):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MemberDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# Route Product
class ProductList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        # data = request.data
        # member_id = data.get('member_id')
        # if member_id is None:
        #     return Response({"member_id": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     member = Member.objects.get(pk=member_id)
        # except Exception:
        #     return Response({"member_id":"Not found member_id."},status=status.HTTP_404_NOT_FOUND)
        
        # print('memberfinnd',member) 
        # # request.data.member = member
        # # print('data.member_id',data.member_id) 
        # # print('self',Member.objects.get(pk=data.member_id)) 
        # # print('request',Member.getob) 
        # # return Response({"member_id":member},status=status.HTTP_404_NOT_FOUND)

        # # return Response({"member_id":"Not found member_id."},status=status.HTTP_404_NOT_FOUND)
        # # data.owner = member
        # data2 = {**data, "owner": MemberSerializer(member).data }
        # print('request.data',{**data, "owner": MemberSerializer(member).data })
        # request.data = {**request.data, **data2}
        # print('request.data2',request.data)

        return self.create(request, *args, **kwargs)

class ProductDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# Route Order
class OrderList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView,):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class OrderDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# Route OrderToProduct
class OrderToProductList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView,):
    queryset = OrderToProduct.objects.all()
    serializer_class = OrderToProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class OrderToProductDetail(APIView):
    queryset = OrderToProduct.objects.all()
    serializer_class = OrderToProductSerializer

    def get_object(self, pk):
        try:
            return OrderToProduct.objects.get(pk=pk)
        except OrderToProduct.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        order_to_project = self.get_object(pk)
        serializer = OrderToProductSerializer(order_to_project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order_to_project = self.get_object(pk)
        serializer = OrderToProductSerializer(order_to_project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        order_to_project = self.get_object(pk)
        order_to_project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Route Discount
class DiscountList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView,):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DiscountDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



