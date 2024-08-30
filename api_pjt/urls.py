from django.contrib import admin
from django.urls import path
from articles import views
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/articles/", include("articles.urls")), # api/api_version/..
]


