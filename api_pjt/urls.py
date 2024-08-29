from articles import views
from django.urls import path


app_name = "articles"
urlpatterns = [
    # http://127.0.0.1:8000/html/http://127.0.0.1:8000/html/
    path("html/", views.article_list_html, name="article_list_html"),
    # http://127.0.0.1:8000/json-01/
    path("json-01/", views.json_01, name="json_01"),
    path("json-02/", views.json_02, name="json_02"),
]