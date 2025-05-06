from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    quotes = models.TextField(blank=True, null=True)
    quotes_author = models.CharField(max_length=300, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            counter = 1
            original_slug = self.slug
            while Blog.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
