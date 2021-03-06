# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 13:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from random import randrange


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0004_auto_20170623_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_from',
            field=models.ForeignKey(default=randrange(1, 6), on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
