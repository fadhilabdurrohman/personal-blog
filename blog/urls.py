from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path("", show_post, name="post_list"),
    path("login/", login_user, name="login")
]