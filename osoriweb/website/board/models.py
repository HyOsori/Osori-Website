from django.db import models
from django.utils import timezone

# Create your models here.

class InfoArticle(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    view_count = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

class InfoComment(models.Model):
    article = models.ForeignKey('board.InfoArticle', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class CommentLikes(models.Model):
	user = models.ForeignKey('auth.User')
	comment = models.ForeignKey('board.InfoComment', related_name='likes')
	created_date = models.DateTimeField(default = timezone.now)