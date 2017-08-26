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
