from rest_framework import viewsets
from .models import User, Producer,Client,Profile
from .serializers import UserSerializer, ProducerSerializer,MyTokenObtainPairSerializer,ClientSerializer,RegisterSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics ,status
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny,IsAuthenticated


# Create viewsets here
class UserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  
    serializer_class = UserSerializer 

class ClientSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()  
    serializer_class = ClientSerializer 

class ProducerSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()  
    serializer_class = ProducerSerializer  

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class =RegisterSerializer
#function to test if the user is authenticated 
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    if request.method == 'GET':
        response = f"Hey {request.user},This is  a GET response"
        return Response({'response':response},status=status.HTTP_200_OK)
    elif  request.method == 'POST':  
        text=request.POST.get("text")
        response=f"Hey {request.user},your text is {text}"
        return Response({"respose":response},status=status.HTTP_200_OK)
    return Response({},status=status.HTTP_400_BAD_REQUEST)
