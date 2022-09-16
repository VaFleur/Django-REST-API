from rest_framework import serializers
from .models import Article, Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'type_name', 'type_color']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'type', 'article_name', 'short_desc', 'full_desc']
        depth = 1
