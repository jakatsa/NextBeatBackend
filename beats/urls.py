from django.urls import path,include
from rest_framework import routers

from .views import(CategoryViewSet,BeatViewSet,LicenseViewSet)

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'beat', BeatViewSet)
router.register(r'license', LicenseViewSet)

urlpatterns =[
    path('api/',include(router.urls))
]