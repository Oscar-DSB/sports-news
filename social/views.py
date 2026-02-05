from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.shortcuts import render

from .models import MemberProfile

@staff_member_required
def members_list(request):
    # Mostramos TODOS los usuarios con su perfil (si falta alguno lo creamos)
    User = get_user_model()
    users = User.objects.all().order_by("username")

    # asegurar perfiles para todos
    for u in users:
        MemberProfile.objects.get_or_create(user=u)

    profiles = (
        MemberProfile.objects
        .select_related("user", "watching_sport")
        .order_by("user__username")
    )

    return render(request, "social/members.html", {"profiles": profiles})
