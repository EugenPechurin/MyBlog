# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 22:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170620_1656'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coments',
            new_name='Comments',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='coments_article',
            new_name='comments_article',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='coments_text',
            new_name='comments_text',
        ),
    ]
