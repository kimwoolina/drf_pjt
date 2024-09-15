from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Product, Products
from .serializers import ProductSerializer, ProductsSerializer

from rest_framework.views import APIView



"""
@api_view(["GET"])
def product_list(request):
    cache_key = "product_list"
    # DB에서 데이터를 가져오기 전에 캐시에서 먼저 가져오려고 시도해본다!
    if not cache.get(cache_key): # 캐시에 없을 경우 데이터베이스에서 조회 (cache miss)
        print("cache miss")
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        json_response = serializer.data
        cache.set(cache_key, json_response, 180)
    
    json_response = cache.get(cache_key) # 캐시에 있을 경우 캐시에서 가져온다 -> 반정도로 실행시간 줄어든다!
    return Response(json_response)
"""

class ProductListView(APIView):
    
    # 상품 등록은 로그인 상태 필요, 상품 목록 조회는 로그인 없이 가능하게
    permission_classes = [IsAuthenticatedOrReadOnly]
    # 클릭해서 코드 확인해보면, SAFE_METHODS('GET', 'HEAD', 'OPTIONS') == 데이터를 조작하지 않아 안전한 요청들은 인증 불필요하게.
    
    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        # Postman에서 image필드는 json으로 보낼수가 없음. -> Body의 form-data사용하면 이미지도 올릴 수 있다!
        image = request.data.get('image')
        
        print(title, content, image)
        
        # product = Product.objects.create(**request.data)와 같음
        product = Products.objects.create(title=title, content=content, image=image)
        
        serializer = ProductsSerializer(product)
        
        return Response(serializer.data)
    
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)