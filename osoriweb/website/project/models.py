from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    start_period = models.CharField(max_length=8)
    end_period = models.CharField(max_length=8, blank=True, null=True)
    github_url = models.URLField()
    contributor = models.CharField(max_length=200)

    def __str__(self):
        return self.title