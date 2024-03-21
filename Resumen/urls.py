from django.urls import include, path
from Resumen import views as resumeViews

urlpatterns = [
    path("stadistics/", resumeViews.resume, name="stadistics"),
]
