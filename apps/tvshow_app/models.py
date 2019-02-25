from __future__ import unicode_literals
from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Description should be at least 10 characters"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    date = models.DateField()
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
