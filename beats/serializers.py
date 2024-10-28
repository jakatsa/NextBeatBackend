from rest_framework import serializers
from .models import Category, Beat, License

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BeatSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())  # Writable field

    class Meta:
        model = Beat
        fields = '__all__'
        read_only_fields = ['slug']
class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'
