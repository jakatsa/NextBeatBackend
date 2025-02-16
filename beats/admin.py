from django.contrib import admin
from .models import Category, Beat, License

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(Beat)
class BeatAdmin(admin.ModelAdmin):
    list_display = ('title', 'producer', 'price', 'created_at')
    list_filter = ('genre', 'created_at', 'producer')
    search_fields = ('title', 'genre', 'producer__username')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('categories',)

@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('beat', 'type', 'price')
    list_filter = ('type',)
    search_fields = ('beat__title',)
