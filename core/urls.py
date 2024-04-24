from django.urls import include, path
from core import views as coreViews

urlpatterns = [
    path("", coreViews.front_view, name="front"),
    path("acerca/", coreViews.acerca, name="acerca"),
    path("/login/", coreViews.login, name="login"),
    path("/register/", coreViews.register, name="register"),
]
