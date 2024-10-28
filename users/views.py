from rest_framework import viewsets
from .models import User, Producer
from .serializers import UserSerializer, ProducerSerializer

# Create viewsets here
class UserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # Correct model
    serializer_class = UserSerializer  # Correct serializer

class ProducerSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()  # Correct model
    serializer_class = ProducerSerializer  # Correct serializer
