from django.urls import include, path
from Data import views as DataViews

urlpatterns = [
    path("information/", DataViews.Data_view, name="Datos"),
]
