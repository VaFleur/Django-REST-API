from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ArticleSerializer, TypeSerializer
from .models import Article, Type

# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('article_name')
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        new_article = Article.objects.create(
            type=Type.objects.get(type_name=data["type_name"]),
            article_name=data["article_name"],
            short_desc=data["short_desc"],
            full_desc=data["full_desc"]
        )

        new_article.save()
        serializer = ArticleSerializer(new_article)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        queryset = Article.objects.filter(type__type_name=params["pk"])
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)


class ArticleTypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all().order_by('type_name')
    serializer_class = TypeSerializer

