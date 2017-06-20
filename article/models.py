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

class Coments(models.Model):
    class Meta():
        db_table = 'comments'

    coments_text = models.TextField()
    coments_article = models.ForeignKey(Article)
