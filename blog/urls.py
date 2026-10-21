from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path("", show_post, name="post_list"),
    path("post/<uuid:pk>/", post_detail, name="post"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]
