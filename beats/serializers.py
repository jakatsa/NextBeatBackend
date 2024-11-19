from rest_framework import serializers
from .models import Category, Beat, License,Producer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BeatSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())  # Writable field
    user_name = serializers.CharField(source='producer.user_name', read_only=True)

    class Meta:
        model = Beat
        fields = '__all__'
        read_only_fields = ['slug']
class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'
