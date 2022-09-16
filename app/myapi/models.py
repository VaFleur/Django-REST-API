from django.db import models


class Type(models.Model):
    type_name = models.CharField(max_length=255)
    type_color = models.CharField(max_length=255)

    def __str__(self):
        return self.type_name


class Article(models.Model):
    article_name = models.CharField(max_length=255)
    short_desc = models.CharField(max_length=511)
    full_desc = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, related_name='articles')

    def __str__(self):
        return self.article_name
