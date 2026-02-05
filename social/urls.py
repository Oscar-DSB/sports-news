from django.urls import path
from django.contrib.auth import views as auth_views
from .views import members_list

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="social/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("members/", members_list, name="members_list"),
]
