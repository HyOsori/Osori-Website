from django.db import models
from django.utils import timezone

# Create your models here.
class FreePost(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    view_count = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
	post = models.ForeignKey('board.FreePost', related_name = 'comments')
	author = models.ForeignKey('auth.User')
	text = models.TextField()
	created_date = models.DateTimeField(
	        default=timezone.now)
	published_date = models.DateTimeField(
	        blank=True, null=True)

	def publish(self):
	    self.published_date = timezone.now()
	    self.save()

	def __str__(self):
	    return self.title