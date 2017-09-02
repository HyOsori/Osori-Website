from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


class UserProfile(models.Model):

    user = models.OneToOneField(User, related_name='UserProfile', on_delete=models.CASCADE)

    '''
    username, first_name, last_name, email, password, groups, user_permission, is_staff, is_active, 
    '''
    department = models.CharField(max_length=30, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)  # validators should be a list
    github_id = models.CharField(max_length=30, blank=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.UserProfile.save()


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