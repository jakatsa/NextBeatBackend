from django.db import models

class Configuration(models.Model):
    site_name = models.CharField(max_length=100)
    site_description = models.TextField()
    site_logo = models.ImageField(upload_to='logos')

    def __str__(self):
        return self.site_name
