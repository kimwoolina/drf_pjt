from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        # 이건 읽기전용 필드니까 쓸 때는 건드리지마! -> article 안넣고 content만 넣어도 is_valid 통과함
        read_only_fields = ("article",)
    
    # 보여지는 것만 수정
    # 이렇게 필드 삭제 뿐만 아니라 여기서 필드를 추가할 수도 있겠죠!
    def to_representation(self, instance):
        # super: serializers.ModelSerializer
        ret = super().to_representation(instance)
        ret.pop("article")
        return ret
        


class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = "__all__"


# 목록 조회에서는 댓글이 안보이게 하려면?
# ArticleSerializer 상속으로 간단하게 해결 가능!
class ArticleDetailSerializer(ArticleSerializer):
    
    # 오버라이딩
    # many=True : 하나의 commnent가 아닌 여러개의 comments관한 것이므로
    # read only 해주지 않으면 POST 때 문제 발생
    # comments: 역참조 매니저. comment_set아니고 related_name 붙여줬던것!!
    comments = CommentSerializer(many=True, read_only=True)
    
    # 댓글 수 필드 추가
    # 이건 오버라이딩 아님 # source="comments.count" : ORM임 article.comments.count()
    # source부분 안적어줘도 되는데, 우리는 아는 값이므로 적는 것.
    # 점표기법 : comments(.)count
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)
    # DRF를 쓰는 이유 중 하나. 모델에 대한 의존성 줄이고 Serializer만 사용