from django.shortcuts import render, get_object_or_404

from .models import Blog


# def dashboard(request):
#     template_name = "dashboard/base.html"
#     context = {
#         'title': 'halaman dashboard'
#     }
#     return render(request, template_name, context)

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
