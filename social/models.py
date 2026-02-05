from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MemberProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    watching_sport = models.ForeignKey(
        "sports.Sport",
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="watching_profiles"
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        MemberProfile.objects.create(user=instance)
