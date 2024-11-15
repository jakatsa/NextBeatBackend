from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import (Order, Tax, OrderItem, Cart, CartItem, Payment, Beat, License)
from .serializers import (OrderItemSerializer, CartItemSerializer, 
                          OrderSerializer, TaxSerializer, 
                          CartSerializer, PaymentSerializer)
# Pagination class (optional)
from rest_framework.pagination import PageNumberPagination

class StandardResultsPagination(PageNumberPagination):
    page_size = 10

# Views for CRUD operations
class OrderItemSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.select_related('order', 'beat').all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartItemSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.select_related('cart', 'beat', 'license').all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsPagination

    @action(detail=True, methods=['post'])
    def update_quantity(self, request, pk=None):
        cart_item = self.get_object()
        quantity = request.data.get('quantity')
        if quantity and int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
            return Response({'status': 'Quantity updated'})
        return Response({'error': 'Invalid quantity'}, status=status.HTTP_400_BAD_REQUEST)


class OrderSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('user').prefetch_related('beats').all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaxSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
    permission_classes = [IsAuthenticated]


class CartSet(viewsets.ModelViewSet):
    queryset = Cart.objects.prefetch_related('cart_items').all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsPagination

    @action(detail=True, methods=['post'])
    def add_item(self, request, pk=None):
        cart = self.get_object()
        beat_id = request.data.get('beat_id')
        license_id = request.data.get('license_id')
        quantity = request.data.get('quantity', 1)

        # Check if beat and license exist
        beat = get_object_or_404(Beat, id=beat_id)
        license = get_object_or_404(License, id=license_id)

        # Check if item with the same license already exists in the cart
        existing_item = cart.cart_items.filter(beat=beat, license=license).first()
        if existing_item:
            return Response({'error': 'Item with the same license already in cart'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Create the new cart item
        CartItem.objects.create(cart=cart, beat=beat, license=license, quantity=quantity, price=beat.price)
        return Response({'status': 'Item added to cart'})

    @action(detail=True, methods=['post'])
    def clear_cart(self, request, pk=None):
        cart = self.get_object()
        cart.cart_items.all().delete()
        return Response({'status': 'Cart cleared'})


class PaymentSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related('order').all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
