from django.urls import path,include
from rest_framework import routers
from users import views 
from rest_framework_simplejwt.views import TokenRefreshView


from .views import(
   UserSet, ProducerSet)

router = routers.DefaultRouter()
router.register(r'user',UserSet)
router.register(r'producer',ProducerSet)


urlpatterns =[
    path('api/',include(router.urls)),
    path('v1/token/',views.MyTokenObtainPairView.as_view(), name='token'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("v1/register/",views.RegisterView.as_view(),name='register'),
    path("v1/dashboard/",views.RegisterView.as_view(),name='dashboard')
]