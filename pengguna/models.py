from django.db import models

# Create your models here.

class Biodata(models.Model):
    alamat = models.TextField(blank=True, null = True)
    telp = models.CharField(max_length=20, blank=True, null=True)