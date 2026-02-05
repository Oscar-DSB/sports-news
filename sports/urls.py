from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("sport/f1/", views.f1_ranking, name="f1_ranking"),
    path("sport/<slug:slug>/", views.sport_detail, name="sport_detail"),
    path("match/<int:match_id>/", views.match_detail, name="match_detail"),
]
