from django.urls import path
from berita.views import dashboard, blog_detail, blog

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('', blog, name='blog'),
    path('detail', blog_detail, name='blog_detail'),
]