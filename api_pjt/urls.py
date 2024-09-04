from django.contrib import admin
from django.urls import path
from articles import views
from django.urls.conf import include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    path("api/v1/articles/", include("articles.urls")),  # api/api_version/..
    path("api/v1/accounts/", include("accounts.urls")),
    path("api/v1/products/", include("products.urls")),
    path("api/v1/chatgpt/", include("chatgpt.urls")),
]
urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]

# drf-spectacular (API 문서 작성)
urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"), 
        name="swagger-ui"
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"), 
        name="redoc"
    ),
]
