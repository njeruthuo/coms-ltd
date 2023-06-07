from django.contrib import admin
from django.urls import path, include
from user import utils

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', utils.index, name='index'),
    path('home/', utils.home, name='home'),
    path('apply/<int:pk>/', utils.package_application, name='package-application'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# For serving media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)