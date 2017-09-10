# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 15:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0002_auto_20170831_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='board.InfoArticle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='commentlikes',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='commentlikes',
            name='user',
        ),
        migrations.RemoveField(
            model_name='infocomment',
            name='article',
        ),
        migrations.DeleteModel(
            name='CommentLikes',
        ),
        migrations.DeleteModel(
            name='InfoComment',
        ),
    ]