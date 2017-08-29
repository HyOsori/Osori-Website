# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=200)),
                ('start_period', models.CharField(max_length=8)),
                ('end_period', models.CharField(blank=True, max_length=8, null=True)),
                ('github_url', models.URLField()),
                ('contributor', models.CharField(max_length=200)),
            ],
        ),
    ]