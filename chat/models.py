from django.db import models
from users.models import User, Profile

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_messages") 
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages") 
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages") 
    message = models.CharField(max_length=1000)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']
        verbose_name_plural = "Messages"  # Corrected typo

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.message[:20]}"  # Show only first 20 chars

    @property
    def sender_profile(self): 
        return Profile.objects.get(user=self.sender)

    @property
    def receiver_profile(self): 
        return Profile.objects.get(user=self.receiver)
