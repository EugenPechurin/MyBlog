# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coments_text', models.TextField()),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='article_like',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coments',
            name='coments_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article'),
        ),
    ]
