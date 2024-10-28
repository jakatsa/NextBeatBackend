from rest_framework import serializers
from .models import (Order, Tax, OrderItem, Cart, CartItem, Payment)

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ['subtotal', 'total_price']  # Make these read-only

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields = ['added_at']  # Make added_at read-only

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['created_at', 'status']  # Make these read-only

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']  # Make these read-only

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']  # Make these read-only

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['created_at', 'status']  # Make these read-only
