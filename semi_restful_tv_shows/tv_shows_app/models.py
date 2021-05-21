from django.db import models

# Create your models here.


class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Network(models.Model):
    name = models.CharField(max_length=255)
    shows = models.ManyToManyField(
        Show, related_name="networks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
