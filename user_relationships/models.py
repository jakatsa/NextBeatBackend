# user_relationships/models.py

from django.db import models
from users.models import User

# Follow Model: Represents a follow relationship between a user and a producer.
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    producer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')  # Assuming producers are also Users
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'producer')  # Prevent duplicate follows

    def __str__(self):
        return f"{self.follower.username} follows {self.producer.username}"

# Notification Model: Represents notifications for users.
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    # Add a field to specify notification type
    notification_type = models.CharField(max_length=50, choices=[
        ('new_beat', 'New Beat Added'),
        ('other', 'Other'),  # You can add more types as needed
    ], default='other')

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
