from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import (
    CustomUser,
    CustomUserFilter,
    CustomUserInfo,
    CustomUserSettings,
)


@receiver(post_save, sender=CustomUser)
def create_user_info(sender, instance, created, **kwargs):
    if created:
        CustomUserInfo.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def create_user_settings(sender, instance, created, **kwargs):
    if created:
        CustomUserSettings.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def create_user_filter(sender, instance, created, **kwargs):
    if created:
        CustomUserFilter.objects.create(user=instance)
