from django.db import models


class RegistrationStageChoices(models.TextChoices):
    """Стадия регистрации на мероприятие"""

    PARTICIPATED = ("participated", "Участвовал")
    PARTICIPATING = ("participating", "Участвую")
    NOT_REGISTERED = ("not_registered", "Не зарегистрирован")


class FormatChoices(models.TextChoices):
    """Формат проведения турнира"""

    ONLINE = ("online", "онлайн")
    OFFLINE = ("offline", "оффлайн")
