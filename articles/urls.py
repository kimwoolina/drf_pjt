from django.urls import path
from . import views

#사실 API를 작성할때는 app_name이나, name을 잘 쓰지 않는 편, 겹칠 일이 잘 없기 때문에..
app_name = "articles"

urlpatterns = [
    # path("", views.article_list, name="article_list"),
    path("", views.ArticleListAPIView.as_view(), name="article_list"),
    path("<int:pk>/", views.ArticleDetailAPIView.as_view(), name ="article_detail"),
    path("<int:article_pk>/comments/", views.CommentListAPIView.as_view(), name="comment_list"),
    path("comments/<int:comment_pk>/", views.CommentDetailAPIView.as_view(), name="comment_detail")
]