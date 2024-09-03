from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

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