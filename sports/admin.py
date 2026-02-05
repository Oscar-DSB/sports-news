from django.contrib import admin
from .models import Sport, Team, Match


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "active")
    list_filter = ("active",)
    search_fields = ("name", "slug")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("sport", "date", "time", "status", "home_team", "away_team", "home_score", "away_score")
    list_filter = ("sport", "status", "date")
    search_fields = ("home_team__name", "away_team__name")
    ordering = ("-date", "-time")
