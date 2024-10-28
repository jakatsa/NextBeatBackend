from django.urls import path,include
from rest_framework import routers

from .views import(
   UserSet, ProducerSet)

router = routers.DefaultRouter()
router.register(r'user',UserSet)
router.register(r'producer',ProducerSet)


urlpatterns =[
    path('api/',include(router.urls))
]