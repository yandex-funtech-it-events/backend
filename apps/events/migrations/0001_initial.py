# Generated by Django 4.2 on 2024-04-16 14:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Events",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "registration_open",
                    models.DateTimeField(
                        db_index=True,
                        default=None,
                        verbose_name="дата открытия регистрации",
                    ),
                ),
                (
                    "registration_close",
                    models.DateTimeField(
                        db_index=True,
                        default=None,
                        verbose_name="дата закрытия регистрации",
                    ),
                ),
                (
                    "date_start",
                    models.DateField(
                        db_index=True,
                        default=None,
                        verbose_name="дата начала мероприятия",
                    ),
                ),
                (
                    "date_end",
                    models.DateField(
                        db_index=True,
                        default=None,
                        verbose_name="дата окончания мероприятия",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="название"
                    ),
                ),
                (
                    "description",
                    models.TextField(max_length=500, verbose_name="описание"),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=20,
                        verbose_name="город мероприятия",
                    ),
                ),
                (
                    "picture",
                    models.ImageField(
                        blank=True,
                        upload_to="events_pictures/",
                        verbose_name="обложка мероприятия",
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="адрес мероприятия"
                    ),
                ),
                (
                    "format",
                    models.CharField(
                        choices=[("online", "онлайн"), ("offline", "оффлайн")],
                        max_length=7,
                        verbose_name="формат мероприятия",
                    ),
                ),
                (
                    "stream_link",
                    models.URLField(
                        blank=True, default="", verbose_name="ссылка на трансляцию"
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events_created",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="организатор",
                    ),
                ),
                (
                    "moderator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events_moderated",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="модератор",
                    ),
                ),
            ],
            options={
                "verbose_name": "мероприятие",
                "verbose_name_plural": "мероприятия",
                "ordering": ("id", "created_at", "creator"),
            },
        ),
        migrations.CreateModel(
            name="EventTags",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="тег мероприятия",
                    ),
                ),
            ],
            options={
                "verbose_name": "тег",
                "verbose_name_plural": "теги",
            },
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "topic",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="название доклада"
                    ),
                ),
                (
                    "short_description",
                    models.TextField(
                        max_length=500, unique=True, verbose_name="описание долкада"
                    ),
                ),
                (
                    "start_at",
                    models.DateTimeField(
                        db_index=True, default=None, verbose_name="дата начала доклада"
                    ),
                ),
                (
                    "end_at",
                    models.DateTimeField(
                        db_index=True,
                        default=None,
                        verbose_name="дата окончания доклада",
                    ),
                ),
                (
                    "speaker",
                    models.CharField(
                        max_length=50, verbose_name="Фамилиия и имя спикера"
                    ),
                ),
                (
                    "position",
                    models.CharField(max_length=50, verbose_name="Должность спикера"),
                ),
                (
                    "speaker_photo",
                    models.ImageField(
                        blank=True,
                        upload_to="speakers_pictures/",
                        verbose_name="Фотография спикера",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reported_at_event",
                        to="events.events",
                        verbose_name="доклад",
                    ),
                ),
            ],
            options={
                "verbose_name": "Доклад",
                "verbose_name_plural": "Доклады",
                "ordering": ["-start_at"],
            },
        ),
        migrations.CreateModel(
            name="Registration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "registration_stage",
                    models.CharField(
                        choices=[
                            ("participated", "Участвовал"),
                            ("participating", "Участвую"),
                            ("not_registered", "Не зарегистрирован"),
                        ],
                        default="not_registered",
                        max_length=20,
                        verbose_name="стадия регистрации",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="registrated_event",
                        to="events.events",
                        verbose_name="мероприятие",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="participants",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="участник",
                    ),
                ),
            ],
            options={
                "verbose_name": "Регистрация",
                "verbose_name_plural": "Регистрации",
            },
        ),
        migrations.CreateModel(
            name="Favorites",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="event_favorite",
                        to="events.events",
                        verbose_name="мероприятие",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="participants_favorite",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="участник",
                    ),
                ),
            ],
            options={
                "verbose_name": "избранное мероприятие",
                "verbose_name_plural": "избранные мероприятия",
            },
        ),
        migrations.AddField(
            model_name="events",
            name="tags",
            field=models.ManyToManyField(to="events.eventtags", verbose_name="тег"),
        ),
    ]
