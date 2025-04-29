from django.contrib import admin
from django.urls import path, include

from mysite.views import home, about
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name="home"),
    # path('dashboard/', include("berita.urls")),
    path('blog/', include("berita.urls")),
]