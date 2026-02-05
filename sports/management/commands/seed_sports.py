from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Seed sports data (deportes, equipos y partidos)"

    def handle(self, *args, **options):
        # Import dentro para asegurar que Django está cargado
        from django.utils import timezone
        from datetime import timedelta
        from random import randint, choice
        from sports.models import Sport, Team, Match

        def get_or_create_sport(name, slug, icon):
            s, _ = Sport.objects.get_or_create(
                slug=slug,
                defaults={"name": name, "icon": icon, "active": True}
            )
            s.name = name
            s.icon = icon
            s.active = True
            s.save()
            return s

        def get_team(name):
            t, _ = Team.objects.get_or_create(name=name)
            return t

        def make_scores(slug):
            if slug == "baloncesto":
                return randint(80, 130), randint(80, 130), ""
            if slug == "futbol":
                return randint(0, 5), randint(0, 5), ""
            if slug == "nfl":
                return randint(10, 38), randint(10, 38), ""
            if slug == "tenis":
                return None, None, choice([
                    "6-3 3-6 7-6",
                    "6-4 6-2",
                    "7-6 6-7 6-4",
                    "6-1 6-3",
                ])
            if slug == "padel":
                return None, None, choice([
                    "6-4 3-6 6-3",
                    "6-2 6-4",
                    "7-6 6-7 6-4",
                    "6-3 6-3",
                ])
            if slug == "boxeo":
                return None, None, choice([
                    "Gana por KO (R8)",
                    "Gana por KO (R3)",
                    "Gana por decisión unánime",
                    "Gana por TKO (R6)",
                ])
            return randint(0, 3), randint(0, 3), ""

        # Deportes
        sports = [
            ("Baloncesto", "baloncesto", "🏀"),
            ("Boxeo", "boxeo", "🥊"),
            ("F1", "f1", "🏎️"),
            ("Fútbol", "futbol", "⚽"),
            ("NFL", "nfl", "🏈"),
            ("Pádel", "padel", "🎾"),
            ("Tenis", "tenis", "🎾"),
        ]
        sport_objs = {slug: get_or_create_sport(name, slug, icon) for name, slug, icon in sports}

        teams_by_sport = {
            "baloncesto": ["Celtics", "Heat", "Knicks", "Bulls", "Warriors", "Nets"],
            "futbol": ["Betis", "Sevilla", "Real Madrid", "Barcelona", "Atlético", "Valencia"],
            "nfl": ["Dolphins", "Commanders", "Chiefs", "Eagles", "49ers", "Bills"],
            "tenis": ["Alcaraz", "Sinner", "Djokovic", "Medvedev", "Zverev", "Ruud"],
            "padel": ["Paquito", "Coello", "Galán", "Lebrón", "Tapia", "Chingotto"],
            "boxeo": ["Fury", "Joshua", "Usyk", "Tank", "Bivol", "Inoue"],
        }

        # Limpia partidos antiguos (demo)
        Match.objects.all().delete()

        now = timezone.localtime()
        today = timezone.localdate()

        for slug, sport in sport_objs.items():
            if slug == "f1":
                continue  # F1 se muestra con template especial

            names = teams_by_sport.get(slug, ["A", "B", "C", "D"])
            teams = [get_team(n) for n in names]

            def pick_two():
                a = choice(teams)
                b = choice([x for x in teams if x != a])
                return a, b

            # 2 anteriores
            for _ in range(2):
                a, b = pick_two()
                d = today - timedelta(days=randint(1, 7))
                t = (now - timedelta(hours=randint(2, 10))).time().replace(second=0, microsecond=0)
                hs, as_, txt = make_scores(slug)
                Match.objects.create(
                    sport=sport, home_team=a, away_team=b,
                    date=d, time=t, status="finished",
                    home_score=hs, away_score=as_, result_text=txt
                )

            # Hoy: 2 finished, 1 live, 1 scheduled
            for _ in range(2):
                a, b = pick_two()
                past_time = (now - timedelta(hours=randint(2, 6))).time().replace(second=0, microsecond=0)
                hs, as_, txt = make_scores(slug)
                Match.objects.create(
                    sport=sport, home_team=a, away_team=b,
                    date=today, time=past_time, status="finished",
                    home_score=hs, away_score=as_, result_text=txt
                )

            a, b = pick_two()
            live_time = (now - timedelta(minutes=15)).time().replace(second=0, microsecond=0)
            hs, as_, txt = make_scores(slug)
            Match.objects.create(
                sport=sport, home_team=a, away_team=b,
                date=today, time=live_time, status="live",
                home_score=hs, away_score=as_, result_text=txt
            )

            a, b = pick_two()
            future_time = (now + timedelta(hours=randint(1, 6))).time().replace(second=0, microsecond=0)
            Match.objects.create(
                sport=sport, home_team=a, away_team=b,
                date=today, time=future_time, status="scheduled",
                home_score=None, away_score=None, result_text=""
            )

            # 2 próximos
            for _ in range(2):
                a, b = pick_two()
                d = today + timedelta(days=randint(1, 10))
                t = (now + timedelta(hours=randint(2, 10))).time().replace(second=0, microsecond=0)
                Match.objects.create(
                    sport=sport, home_team=a, away_team=b,
                    date=d, time=t, status="scheduled",
                    home_score=None, away_score=None, result_text=""
                )

        self.stdout.write(self.style.SUCCESS("✅ Seed completado: deportes y partidos coherentes."))
