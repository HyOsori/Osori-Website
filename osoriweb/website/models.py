from django.db import models
from django.utils import timezone


class Inquiry(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	title = models.CharField(max_length=200)
	content = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	answered = models.BooleanField(default=False)

	def __str__(self):
		return self.title

class History(models.Model):
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    content = models.TextField()

    def __str__(self):
        return year + ". " + month