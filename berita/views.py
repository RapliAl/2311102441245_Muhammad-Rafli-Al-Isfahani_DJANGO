from django.shortcuts import render
from .models import Blog

# Create your views here.

def dashboard(request):
    template_name = "halaman/base.html"
    context = {
        'title': 'halaman dashboard'
    }
    return render(request, template_name, context)

def blog (request):
    template_name = "halaman/base.html"
    context = {
        'title': 'blog'
    }
    return render(request, template_name, context)

def blog_detail (request):
    blog = Blog.objects.all()

    return render(request, 'halaman/detail.html', {'blog': Blog})