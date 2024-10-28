from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)  # Slug field
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not provided
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Beat(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)  # Slug field
    audio_file = models.FileField(upload_to='beats/')
    image = models.ImageField(upload_to='beats/images/', blank=True, null=True)  # New image field
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='beats', blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not provided
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class License(models.Model):
    beat = models.ForeignKey(Beat, on_delete=models.CASCADE, related_name='licenses')
    type = models.CharField(max_length=50, choices=[('exclusive', 'Exclusive'), ('non-exclusive', 'Non-Exclusive')])
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.type} License for {self.beat.title}"
