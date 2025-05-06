from django.urls import path

from berita.views import blog_detail, Blog

urlpatterns = [
    # path('dashboard/', dashboard, name='dashboard'),
    path('', Blog, name='Blog'),

    path('detail/<slug:slug>/', blog_detail, name='blog_detail'),

]
