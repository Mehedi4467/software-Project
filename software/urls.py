
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('User/', include('UserApp.urls')),
    path('Profile/', include('user_profile.urls')),
    path('ticket_counter/', include('counter.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
