# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 14:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('view_count', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('type', models.CharField(choices=[('free', '자유게시판'), ('info', '정보게시판'), ('noti', '공지게시판')], default='noti', max_length=10, verbose_name='게시판 종류')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
