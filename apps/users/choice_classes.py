from django.db import models


class RoleChoices(models.TextChoices):
    """Определение роли юзера."""

    ATTENDEE = ("attendee", "Участник")
    ORGANIZER = ("organizer", "Организатор")
    MODERATOR = ("moderator", "Модератор")


class ExperienceChoices(models.TextChoices):
    """Указание опыта юзера."""

    LESS_1 = ("0-1", "0-1 год")
    MORE_1_LESS_3 = ("1-3", "1-3 года")
    MORE_3_LESS_5 = ("3-5", "3-5 лет")
    MORE_5_LESS_10 = ("5-10", "5-10 лет")
    MORE_10 = ("10+", "Больше 10 лет")
