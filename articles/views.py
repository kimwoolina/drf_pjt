from django.shortcuts import render
from .models import Article
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer #내가만든 Serializer
from django.shortcuts import get_object_or_404



# drf의 함수로 만드는 뷰는 반드시 api 데코레이터(Wrapping method - 함수 실행 전, 후에 실행해준다.) 필요
#@api_view() 안에 안넣어주면 GET,  # ["GET","POST"]
@api_view(["GET"])
def article_list(request):
    articles = Article.objects.all()
    # articles가 1개보다 많을때는 반드시 many=True 적어줘야함
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    serializers = ArticleSerializer(article)
    return Response(serializers.data)
