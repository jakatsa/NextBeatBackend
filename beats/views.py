from django.shortcuts import render
from rest_framework import viewsets
from .models import (Category, Beat, License)
from .serializers import (CategorySerializer,BeatSerializer,LicenseSerializer)
# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer

class BeatViewSet(viewsets.ModelViewSet):
    queryset = Beat.objects.all()
    serializer_class=BeatSerializer    

class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class=LicenseSerializer    
