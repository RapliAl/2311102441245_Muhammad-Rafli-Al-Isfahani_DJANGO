from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from mysite.views import home, about, contact
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)