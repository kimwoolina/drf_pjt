from django.contrib import admin
from django.urls import path
from articles import views
from django.urls.conf import include


urlpatterns = [
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    path("api/v1/articles/", include("articles.urls")), # api/api_version/..
    path("api/v1/accounts/", include("accounts.urls")),
    path("api/v1/products/", include("products.urls")),
]
urlpatterns += [ path("silk/", include("silk.urls", namespace="silk"))]


