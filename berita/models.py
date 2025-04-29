from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=300)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/')


# class Artikel(models.Model):
#     object = None
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     author = models.ForeignKey(User, on_delete=models.PROTECT)
#     image = models.ImageField(upload_to='artikel',blank=True, null=True)
#
#     class Meta:
#         verbose_name_plural = "1. Artikel"
