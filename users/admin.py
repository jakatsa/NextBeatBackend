from django.contrib import admin
from users.models import User, Profile, Client, Producer  

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'full_name', 'verified']    

class ClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_name']

class ProducerAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_name', 'contacts', 'bank_details', 'created_at', 'updated_at']

# Register models
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Producer, ProducerAdmin)
