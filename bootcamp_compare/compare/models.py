from django.db import models
from django.utils import timezone

# Create your models here.

class Camp(models.Model):
    id = models.TextField(primary_key=True)
    name = models.CharField(max_length=256)
    cost = models.CharField(max_length=10)
    length = models.CharField(max_length=56)
    languages = models.TextField()
    etype = models.CharField(max_length=256)
    erate = models.CharField(max_length=6)
    internship = models.CharField(max_length=56)
    loc = models.TextField()
    desc = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
