from datetime import date as dt_date
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Sport, Match
from social.models import MemberProfile
from django.contrib.auth.decorators import login_required


def home(request):
    sports = Sport.objects.filter(active=True).order_by("name")
    return render(request, "sports/home.html", {"sports": sports})


def sport_detail(request, slug):
    sport = get_object_or_404(Sport, slug=slug, active=True)

    if sport.slug == "f1":
        return f1_ranking(request)

    filtro = request.GET.get("filter", "today")
    today = timezone.localdate()

    qs = Match.objects.filter(sport=sport)

    if filtro == "prev":
        qs = qs.filter(date__lt=today).order_by("-date", "-time")
        title = "Anteriores"
    elif filtro == "next":
        qs = qs.filter(date__gt=today).order_by("date", "time")
        title = "Próximos"
    else:
        qs = qs.filter(date=today)
        # orden lógico hoy
        status_rank = {"finished": 0, "live": 1, "scheduled": 2}
        matches = list(qs)
        matches.sort(key=lambda m: (status_rank.get(m.status, 9), m.time))
        qs = matches
        title = "Hoy"

    sports_with_text = {"tenis", "padel", "boxeo"}

    return render(
        request,
        "sports/sport_detail.html",
        {"sport": sport, "filtro": filtro, "title": title, "matches": qs, "sports_with_text": sports_with_text},
    )


def match_detail(request, match_id):
    m = get_object_or_404(Match, id=match_id)
    sports_with_text = {"tenis", "padel", "boxeo"}
    return render(request, "sports/match_detail.html", {"m": m, "sports_with_text": sports_with_text})


def f1_ranking(request, slug="f1"):
    sport = get_object_or_404(Sport, slug=slug, active=True)

    # Datos “mock” coherentes para la UI (como tu foto)
    standings = [
        {"pos": 1, "driver": "Verstappen", "team": "Red Bull", "points": 250, "gap": ""},
        {"pos": 2, "driver": "Hamilton", "team": "Ferrari", "points": 232, "gap": "+18 pts"},
        {"pos": 3, "driver": "Leclerc", "team": "Ferrari", "points": 210, "gap": "+40 pts"},
        {"pos": 4, "driver": "Norris", "team": "McLaren", "points": 198, "gap": "+52 pts"},
        {"pos": 5, "driver": "Sainz", "team": "Williams", "points": 170, "gap": "+80 pts"},
        {"pos": 6, "driver": "Alonso", "team": "Aston Martin", "points": 160, "gap": "+90 pts"},
        {"pos": 7, "driver": "Piastri", "team": "McLaren", "points": 145, "gap": "+105 pts"},
        {"pos": 8, "driver": "Russell", "team": "Mercedes", "points": 130, "gap": "+120 pts"},
        {"pos": 9, "driver": "Perez", "team": "Red Bull", "points": 120, "gap": "+130 pts"},
        {"pos": 10, "driver": "Gasly", "team": "Alpine", "points": 98, "gap": "+152 pts"},
    ]

    calendar = [
        {"date": "22 Ene 2026", "gp": "GP Abu Dhabi", "place": "Yas Marina"},
        {"date": "11 Feb 2026", "gp": "GP Japón", "place": "Suzuka"},
        {"date": "02 Mar 2026", "gp": "GP España", "place": "Barcelona"},
        {"date": "20 Mar 2026", "gp": "GP Francia", "place": "Paul Ricard"},
    ]

    return render(
        request,
        "sports/f1_ranking.html",
        {"sport": sport, "standings": standings, "calendar": calendar},
    )
