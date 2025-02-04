from rest_framework import serializers
from .models import User, Producer, Client, Profile
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['date_joined']  # Make date_joined read-only

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Safe access to related objects
        profile = getattr(user, 'profile', None)
        producer = getattr(user, 'producer', None)
        client = getattr(user, 'client', None)

        if profile:
            token['full_name'] = user.profile.full_name
            token['bio'] = user.profile.bio
            token['verified'] = user.profile.verified
            token['image'] = user.profile.image.url if user.profile.image else None
            token['social_links'] = user.profile.social_links

        if producer:
            token['user_name'] = user.producer.user_name  
            token['bank_details'] = user.producer.bank_details
            token['contacts'] = user.producer.contacts

        if client:
            token['client_user_name'] = user.client.user_name 

        # Basic user details
        token['name'] = user.name
        token['email'] = user.email

        return token

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']  # Make timestamps read-only

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'    
        read_only_fields = ['image']    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password]) 
    password2 = serializers.CharField(write_only=True, required=True)   
    role = serializers.ChoiceField(choices=User.PROFILE_CHOICES, required=True)   
    user_name = serializers.CharField(required=False)  # Optional for producers
    contacts = serializers.CharField(required=False)  # Optional for producers
    bank_details = serializers.CharField(required=False)  # Optional for producers

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'password2', 'role', 'user_name', 'contacts', 'bank_details']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords don't match"})
        
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "A user with this email already exists."})
        
        return attrs                

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            role=validated_data['role']
        )    
        user.set_password(validated_data['password'])  # Hash password
        user.save()

        # Create related objects based on role
        if user.role == 'producer':
            Producer.objects.create(
                user=user,
                user_name=validated_data.get('user_name', ''),
                contacts=validated_data.get('contacts', ''),
                bank_details=validated_data.get('bank_details', '')
            )
        elif user.role == 'client':
            Client.objects.create(
                user=user,
                user_name=validated_data.get('user_name', '')  # Assign user_name to Client
            )

        return user
