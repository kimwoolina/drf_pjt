from django.urls import path
from . import views

urlpatterns = [
    # path("", views.product_list), # 상품목록조회
    path("", views.ProductListView.as_view(), name="product_list"), # 상품등록
]
