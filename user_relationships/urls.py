from django.urls import path,include
from rest_framework import routers

from .views import(
   FollowSet,NotificationSet)

router = routers.DefaultRouter()
router.register(r'Follow',FollowSet)
router.register(r'notification',NotificationSet)


urlpatterns =[
    path('api/',include(router.urls))
]