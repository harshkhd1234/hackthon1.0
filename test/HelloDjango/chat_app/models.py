from django.db import models

# Create your models here.

from django.conf import settings
from django.utils import timezone


class Post(models.Model):

    username= models.CharField(max_length=200)
    message = models.TextField()
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.message