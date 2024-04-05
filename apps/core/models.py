from django.db import models


class TimeStamp(models.Model):
    """Модель временных меток"""

    created_at = models.DateTimeField("дата создания", auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField("дата обновления", auto_now=True, db_index=True)

    class Meta:
        abstract = True


class EventTimeStamp(models.Model):
    """Модель временных меток для events"""

    created_at = models.DateTimeField("дата создания", auto_now_add=True, db_index=True)
    registration_open = models.DateTimeField(
        "дата открытия регистрации", default=None, db_index=True
    )
    registration_close = models.DateTimeField(
        "дата закрытия регистрации", default=None, db_index=True
    )
    date_start = models.DateField(
        "дата начала мероприятия", default=None, db_index=True
    )
    date_end = models.DateField(
        "дата окончания мероприятия", default=None, db_index=True
    )

    class Meta:
        abstract = True
