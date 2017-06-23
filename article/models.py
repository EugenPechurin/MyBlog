from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_like = models.IntegerField(default=0)

    class Meta:
        db_table = "article"

    def __str__(self):
        return str(self.article_title)


class Comments(models.Model):
    class Meta:
        db_table = 'comments'

    comments_date = models.DateTimeField(auto_now=True)
    comments_text = models.TextField(verbose_name="Текст коментария")
    comments_article = models.ForeignKey(Article)
    comments_from = models.ForeignKey(User)
