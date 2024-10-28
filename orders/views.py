from django.shortcuts import render
from rest_framework import viewsets
from .models import (Order, Tax, OrderItem, Cart, CartItem, Payment)
from .serializers import (OrderItemSerializer,CartItemSerializer,OrderSerializer,TaxSerializer,CartSerializer,PaymentSerializer)
# Create your views here.
class OrderItemSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class CartItemSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer    


class OrderSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer     

class TaxSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer  

class CartSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer     

class PaymentSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer     
