from django.db import models
from django.utils import timezone


class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title