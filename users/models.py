from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)  # Save the user first

        try:
            # Automatically create related models based on user role
            if user.role == 'client':
                Client.objects.create(user=user)
            elif user.role == 'producer':
                Producer.objects.create(user=user)
            Profile.objects.create(user=user)  # Create Profile for every user
        except Exception as e:
            # Log the error or handle it appropriately
            print(f"Error creating related models: {e}")
            user.delete()  # Rollback user creation if related models fail
            raise

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    PROFILE_CHOICES = [
        ('producer', 'Producer'),
        ('client', 'Client'),
        ('admin', 'Admin'),
    ]
    
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=PROFILE_CHOICES, default='client')  # Use role choices
    is_staff = models.BooleanField(default=False)  # Add this to enable admin access
    is_superuser = models.BooleanField(default=False) 

    objects = UserManager()  # Link the custom manager

    USERNAME_FIELD = 'email'  # Use email as the username
    REQUIRED_FIELDS = ['name']  # Other fields required for creating a user

    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.name} - Client" 
    

class Producer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contacts = models.CharField(max_length=255, blank=True, null=True)
    bank_details = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.name} - Producer"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    social_links = models.JSONField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='beats/images/', blank=True, null=True) 
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.name} - {self.full_name}"

# Automatically create a profile for a user
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not Profile.objects.filter(user=instance).exists():
        Profile.objects.create(user=instance, full_name=instance.name)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()



