from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('ping/', views.Pong.as_view()),

    path('members/', views.MemberList.as_view()),
    path('members/<int:pk>/', views.MemberDetail.as_view(), name='member_detail'),

    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),

    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>/', views.OrderDetail.as_view()),

    path('order_to_products/', views.OrderToProductList.as_view()),
    path('order_to_products/<int:pk>/', views.OrderToProductDetail.as_view()),

    path('discounts/', views.DiscountList.as_view()),
    path('discounts/<int:pk>/', views.DiscountDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
