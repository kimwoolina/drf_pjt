from django.shortcuts import render
from .models import Article, Comment
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    ArticleSerializer, 
    ArticleDetailSerializer, 
    CommentSerializer 
)#내가만든 Serializer
from django.shortcuts import get_object_or_404

# 함수형, 클래스형 중 뭐가 좋다, 나쁘다 말할 수는 없지만, CBV를 사용하면 우리가 작성하는 코드가 많이 줄어든다.
# 많은 부분을 CBV에 위임하기 때문.
# 보통 간단한 로직(ex.로그인만 처리, 비밀번호 검증만) -> 주로 함수형 사용
# 나눠서 써야하는 경우, 다른곳에있는 클래스를 상속받아서 만드는 경우 -> 클래스형 뷰 사용

class ArticleListAPIView(APIView):
    
    # Get과 Post를 다른 메소드로 분기하여 처리가 가능
    # get, post 메소드만 존재하므로 그외의 요청이 들어오면 not Allowed 자동으로 return
    
    def get(self, request):
        articles = Article.objects.all()
        serializers = ArticleSerializer(articles, many=True)
        return Response(serializers.data)
        
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
class ArticleDetailAPIView(APIView):
    
    # 2번이상 반복되는 부분은 함수로 따로 빼주는 것이 좋다.
    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)
    
    def get(self, requesst, pk):
        article = self.get_object(pk)
        serializers = ArticleDetailSerializer(article)
        return Response(serializers.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        # partial: 일부 필드만 수정 가능하게
        serializer = ArticleDetailSerializer(article, data=request.data, partial= True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, requesst, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CommentListAPIView(APIView):
    def get(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            #이 부분은 커스텀 가능(Response 안에 값 안써줘도됨)
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        
        
class CommentDetailAPIView(APIView):
    
    def get_object(self, comment_pk):
        return get_object_or_404(Comment, pk=comment_pk)
    
    def delete(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        #comment는 필드가 content하나이므로 partial 굳이 안써줘도됨
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        
        
# drf의 함수로 만드는 뷰는 반드시 api 데코레이터(Wrapping method - 함수 실행 전, 후에 실행해준다.) 필요
#@api_view() 안에 안넣어주면 GET,  # ["GET","POST"]
#게시글 목록, 생성 (서로 같은 URL)
# @api_view(["GET", "POST"])
# def article_list(request):
#     # 목록
#     if request.method == "GET":
#         articles = Article.objects.all()
#         # articles가 1개보다 많을때는 반드시 many=True 적어줘야함
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
    
#     # 생성
#     elif request.method == "POST":
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             # 상태코드는 회사에서 협의한 것으로 (200 or 201)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# @api_view(["GET", "PUT", "DELETE"])
# def article_detail(request, pk):
#     if request.method == "GET":
#         article = get_object_or_404(Article, id=pk)
#         serializers = ArticleSerializer(article)
#         return Response(serializers.data)

#     elif request.method == "PUT":
#         article = get_object_or_404(Article, pk=pk)
#         # partial: 일부 필드만 수정 가능하게
#         serializer = ArticleSerializer(article, data=request.data, partial= True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        
    
#     elif request.method == "DELETE":
#         article = get_object_or_404(Article, pk=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)