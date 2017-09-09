from django.db import models
from django.utils import timezone


class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='album')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{id}_{title}'.format(id=self.id, title=self.title)
