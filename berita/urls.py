from django.urls import path

from berita.views import blog_detail, Blog, dashboard, blog_login, blog_signup

urlpatterns = [

    path('dashboard/', dashboard, name='dashboard'),

    path('', Blog, name='Blog'),

    path('detail/<slug:slug>/', blog_detail, name='blog_detail'),

    path('login/', blog_login, name='login'),

    path('signup/', blog_signup, name='signup'),

]
