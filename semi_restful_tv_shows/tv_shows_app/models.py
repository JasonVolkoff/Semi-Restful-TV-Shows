
from django.db import models
from datetime import datetime

# Create your models here.


class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data["title"]) < 2:
            errors["title"] = "Title must be at least 2 characters"
        if len(post_data['network']) < 3:
            errors['network'] = "Network must be at least 3 characters"
        if len(post_data['description']) in range(1, 9):
            errors['description'] = "Optional description must be at least 10 characters"
        if datetime.strptime(post_data['releaseDate'], '%Y-%m-%d') > datetime.now():
            errors['releaseDate'] = "Date must be in the past"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
