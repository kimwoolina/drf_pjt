from django.urls import path
from . import views

urlpatterns = [
    # path("", views.product_list),
    path("", views.ProductListView.as_view(), name="product_list"),
]
