from django.urls import path
from Resumen import views as resumeViews

urlpatterns = [
    path("/acerca/", resumeViews.acerca, name="acerca"),
    path("stadistics/", resumeViews.resume, name="stadistics"),
]
