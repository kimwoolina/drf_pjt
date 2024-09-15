from django.urls import path
from . import views

urlpatterns = [
    # path("", views.product_list), # 상품목록조회
    path("", views.ProductListAPIView.as_view(), name="product_list"), # 상품등록(post), 상품목록조회 및 검색(get)
    path("category/", views.CategoryListView.as_view(), name="category_list"),
]
