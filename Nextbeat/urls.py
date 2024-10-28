from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Importing the app's URLs
import beats.urls  # Assuming each app has its own urls.py
import orders.urls
import users.urls
#import settings.urls
import user_relationships.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beats/', include(beats.urls)),  # Changed from beats.url to beats.urls
    path('orders/', include(orders.urls)),
    path('users/', include(users.urls)),
  #  path('settings/', include(settings.urls)),
    path('relationships/', include(user_relationships.urls)),
]
# Add this to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)