from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    '''
    username, first_name, last_name, email, password, groups, user_permission, is_staff, is_active, 
    '''
    department = models.CharField(max_length=30, blank=False)
    phone_number = models.CharField(max_length=30, blank=False)
    github_id = models.CharField(max_length=30)

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
    id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    content = models.TextField()

    def __str__(self):
        return self.year + ". " + self.month