from django.db import models


class RoleChoices(models.TextChoices):
    """Определение роли юзера."""

    ATTENDEE = ("attendee", "Участник")
    ORGANIZER = ("organizer", "Организатор")
    MODERATOR = ("moderator", "Модератор")


class ExperienceChoices(models.TextChoices):
    """Указание опыта юзера."""

    NO_EXP = ("0", "Нет опыта")
    MORE_1 = ("1", "От 1 года")
    MORE_3 = ("3", "От 3 лет")
    MORE_5 = ("5", "От 5 лет")
    OTHER = ("other", "Другое")
