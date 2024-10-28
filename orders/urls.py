from django.urls import path,include
from rest_framework import routers

from .views import(
    OrderItemSet,CartItemSet,PaymentSet)

router = routers.DefaultRouter()
router.register(r'orderitem',OrderItemSet)
router.register(r'cartitem',CartItemSet)
router.register(r'Payment',PaymentSet)

urlpatterns =[
    path('api/',include(router.urls))
]