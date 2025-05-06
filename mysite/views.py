from django.shortcuts import render

from berita.models import Blog


def home(request):
    blog_data = Blog.objects.all()
    template_name = 'halaman/base.html'
    context = {
        'title': '-HOMEPAGE-',
        'description': 'web portfolio saya',
        'body': 'Halaman home',
        'blogs': blog_data ,
    }
    return render(request, template_name, context )

# def about(request):
#     template_name = 'about.html'
#     context = {
#         'title': '-ABOUT PAGE-',
#         'description': 'web portfolio saya',
#         'body': 'Halaman about'
#     }
#     return render(request, template_name, context)

# def blog(request):
#     blog_data = Blog.objects.all()
#     templates_name = 'halaman/model.html'
#     context = {
#         'blog_data': blog_data,
#     }
#     return render(request, templates_name, context)

def contact(request):
    template_name = 'contact.html'
    context = {
        'title': '- CONTACT -',
        'description': 'Contact',
        'body': 'Contact Page'
    }
    return render(request, template_name, context)