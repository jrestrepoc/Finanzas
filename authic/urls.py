from django.urls import include, path
from authic import views as authicViews

urlpatterns = [
    path("register/", authicViews.register, name="register"),
    path("login/", authicViews.login, name="login"),
]
