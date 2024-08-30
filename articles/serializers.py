from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        # 이건 읽기전용 필드니까 쓸 때는 건드리지마! -> article 안넣고 content만 넣어도 is_valid 통과함
        read_only_fields = ("article",)