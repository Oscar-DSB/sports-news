from django.db import models
from django.utils import timezone


class Sport(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=10, blank=True, default="")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Match(models.Model):
    class Status(models.TextChoices):
        SCHEDULED = "scheduled", "Programado"
        LIVE = "live", "En directo"
        FINISHED = "finished", "Finalizado"

    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name="matches")
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_matches")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_matches")

    # ✅ Esto evita tu error de makemigrations
    date = models.DateField(default=timezone.localdate)
    from datetime import time as time_obj

    time = models.TimeField(default=time_obj(12, 0))

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SCHEDULED)

    home_score = models.IntegerField(null=True, blank=True)
    away_score = models.IntegerField(null=True, blank=True)

    # Para deportes tipo tenis/pádel/boxeo: “6-3 3-6 7-6” o “Fury gana por KO (R8)”
    result_text = models.CharField(max_length=120, blank=True, default="")

    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.sport.slug}: {self.home_team} vs {self.away_team}"

    @property
    def score_label(self):
        if self.home_score is None or self.away_score is None:
            return ""
        return f"{self.home_score} - {self.away_score}"
