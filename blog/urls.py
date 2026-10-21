from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path("", show_post, name="post_list"),
    path("post/<uuid:pk>/", post_detail, name="post"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("create/", create_post, name="create"),
    path("edit/<uuid:pk>/", update_post, name="update"),
    path("delete/<uuid:pk>/", delete_post, name="delete"),
]
