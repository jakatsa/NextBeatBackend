from rest_framework import serializers
from .models import User, Producer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['date_joined']  # Make date_joined read-only

    def validate_email(self, value):
        """
        Custom validation to ensure email is valid and unique.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']  # Make timestamps read-only

    def validate(self, attrs):
        """
        Custom validation to ensure required fields are not empty.
        """
        if not attrs.get('bio'):
            raise serializers.ValidationError("Bio cannot be empty.")
        return attrs
