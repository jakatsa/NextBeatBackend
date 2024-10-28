from rest_framework import serializers
from .models import Follow, Notification

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'
        read_only_fields = ['created_at']  # Make created_at read-only

    def validate(self, attrs):
        """
        Custom validation to ensure a user cannot follow themselves.
        """
        if attrs['follower'] == attrs['producer']:
            raise serializers.ValidationError("You cannot follow yourself.")
        return attrs

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ['created_at', 'is_read']  # Make these read-only

    def validate(self, attrs):
        """
        Custom validation to ensure the notification message is not empty.
        """
        if not attrs.get('message'):
            raise serializers.ValidationError("Notification message cannot be empty.")
        return attrs
