from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog


@login_required
def dashboard(request):
    template_name = "dashboard/index.html"
    context = {
        'title': 'halaman dashboard'
    }
    return render(request, template_name, context)


def blog(request):
    blog_data = Blog.objects.all()
    templates_name = "blog/base.html"
    context = {
        'title': 'Blog',
        'blogs': blog_data,
    }
    return render(request, templates_name, context)


def blog_detail(request, slug):
    blog_data = get_object_or_404(Blog, slug=slug)
    templates_name = "halaman/detail.html"
    context = {
        'blogs': blog_data,
    }
    return render(request, templates_name, context)


def blog_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("Login Successful. User:", user)
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username OR password is incorrect')
    return render(request, 'halaman/login.html')
