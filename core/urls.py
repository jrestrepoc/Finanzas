from django.urls import include, path
from core import views as coreViews

urlpatterns = [
    path("", coreViews.front_view, name="front"),
    path("acerca/", coreViews.acerca_view, name="acerca"),
]
