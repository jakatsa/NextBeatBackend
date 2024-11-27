from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import viewsets
from .models import (Category, Beat, License)
from .serializers import (CategorySerializer,BeatSerializer,LicenseSerializer)
# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer

class BeatFilter(filters.FilterSet):
    # You can filter by ID, title, genre, etc.
    id = filters.NumberFilter(field_name='id', lookup_expr='exact')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')  # Partial matching for title
    genre = filters.CharFilter(field_name='genre', lookup_expr='icontains')  # Partial matching for genre

    class Meta:
        model = Beat
        fields = ['id', 'title', 'genre']
class BeatViewSet(viewsets.ModelViewSet):
    queryset = Beat.objects.all()
    serializer_class=BeatSerializer    
    filter_backends = (filters.DjangoFilterBackend,)  # Use django-filter
    filterset_class = BeatFilter 

class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class=LicenseSerializer    
