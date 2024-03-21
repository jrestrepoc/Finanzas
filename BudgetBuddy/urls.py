
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("", include("authic.urls")),
    path("", include("Resumen.urls")),
    path("", include("Data.urls")),
]
