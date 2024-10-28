from django.shortcuts import render
from rest_framework import viewsets
from .models import Follow, Notification
from .serializers import (FollowSerializer,NotificationSerializer)
# Create your views here.
class  FollowSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

class NotificationSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer    