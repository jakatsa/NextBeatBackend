from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
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
  

    objects = UserManager()  # Link the custom manager

    USERNAME_FIELD = 'email'  # Use email as the username
    REQUIRED_FIELDS = ['name']  # Other fields required for creating a user

    def __str__(self):
        return self.name

class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} - Client" 
    

class Producer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    contacts = models.CharField(max_length=255, blank=True, null=True)
    bank_details = models.TextField(blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_name=models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.name} - Producer"