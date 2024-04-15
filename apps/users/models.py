from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.core.constants import FieldLength
from apps.core.models import TimeStamp
from apps.users import choice_classes


class CustomUser(AbstractUser, TimeStamp):
    """
    Кастомная модель переопределенного юзера.
    При создании пользователя все поля обязательны для заполнения.
    По логике эти данные будут подтягиваться из Яндекс ID.
    """

    username = models.CharField(
        "Имя пользователя",
        unique=True,
        max_length=FieldLength.MAX_LENGTH_USERNAME.value,
    )
    email = models.EmailField(
        "Почта",
        unique=True,
        max_length=FieldLength.MAX_LENGTH_EMAIL.value,
    )
    password = models.CharField(
        "Пароль пользователя",
        max_length=FieldLength.MAX_LENGTH_PASSWORD.value,
    )
    first_name = models.CharField(
        "Имя пользователя",
        max_length=FieldLength.MAX_LENGTH_FIRST_NAME.value,
    )
    last_name = models.CharField(
        "Фамилия пользователя",
        max_length=FieldLength.MAX_LENGTH_LAST_NAME.value,
    )
    phone = models.CharField(
        "Номер телефона пользователя",
        unique=True,
        max_length=FieldLength.MAX_LENGTH_PHONE.value,
    )
    role = models.CharField(
        "Пользовательская роль",
        choices=choice_classes.RoleChoices.choices,
        default=choice_classes.RoleChoices.ATTENDEE,
        max_length=FieldLength.MAX_LENGTH_ROLE.value,
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone", "email"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["-id"]

    def __str__(self):
        return str(self.email)


class Specialization(models.Model):
    """Модель для поля направления работы.

    Описывается следующими полями:
    name - Название направления работы.
    slug - слаг направления работы.
    """

    name = models.CharField(
        "Название",
        unique=True,
        max_length=FieldLength.MAX_NAME.value,
    )
    slug = models.SlugField(
        "Уникальный слаг",
        unique=True,
        max_length=FieldLength.MAX_SLUG.value,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Направление работы"
        verbose_name_plural = "Направления работы"
        ordering = ["name"]


class NotificationTime(models.Model):
    """Модель времени уведомления."""

    name = models.CharField(
        "Название",
        unique=True,
        max_length=255,
    )
    slug = models.SlugField(
        "Уникальный слаг",
        unique=True,
        max_length=255,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Время уведомления"
        verbose_name_plural = "Время уведомления"
        ordering = ["pk"]


class NotificationEventType(models.Model):
    """Модель типа события для уведомления."""

    name = models.CharField(
        "Название",
        unique=True,
        max_length=255,
    )
    slug = models.SlugField(
        "Уникальный слаг",
        unique=True,
        max_length=255,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип события для уведомления"
        verbose_name_plural = "Типы события для уведомления"
        ordering = ["pk"]


class NotificationMethod(models.Model):
    """Модель способа уведомлений."""

    name = models.CharField(
        "Название",
        unique=True,
        max_length=255,
    )
    slug = models.SlugField(
        "Уникальный слаг",
        unique=True,
        max_length=255,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип уведомления"
        verbose_name_plural = "Типы уведомления"
        ordering = ["pk"]


class CustomUserInfo(models.Model):
    """
    Модель для дополнительной информации о пользователе.
    При регистрации личного кабинета все поля обязательны для заполнения.
    """

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="info",
        verbose_name="Пользователь",
    )
    image = models.ImageField(
        "Фото",
        upload_to="users/images/",
        null=True,
        default=None,
        blank=True,
    )
    job = models.CharField(
        "Место работы",
        max_length=FieldLength.MAX_LENGTH_JOB.value,
    )
    experience = models.CharField(
        "Опыт работы",
        choices=choice_classes.ExperienceChoices.choices,
        default=choice_classes.ExperienceChoices.NO_EXP,
        max_length=FieldLength.MAX_LENGTH_EXPERIENCE.value,
    )
    custom_experience = models.CharField(
        "Другой опыт работы",
        max_length=FieldLength.MAX_LENGTH_EXPERIENCE.value,
        blank=True,
        null=True,
    )
    specialization = models.ForeignKey(
        Specialization,
        related_name="users_info",
        on_delete=models.CASCADE,
        verbose_name="Направление работы",
        blank=True,
        null=True,
    )
    user_agree_personal_info = models.BooleanField(
        "Согласие на передачу данных",
        default=False,
    )
    user_agree_publish_cv = models.BooleanField(
        "Согласие на публикацию резюме",
        default=False,
    )
    user_agree_publish_media = models.BooleanField(
        "Согласие на публикацию фото/видео",
        default=False,
    )

    class Meta:
        verbose_name = "Доп. инфо о пользователе"
        verbose_name_plural = "Доп. инфо о пользователях"
        ordering = ["-pk"]

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        if self.experience == choice_classes.ExperienceChoices.OTHER:
            self.experience = self.custom_experience
        super().save(*args, **kwargs)


class CustomUserSettings(models.Model):
    """
    Модель для настроек пользователя в личном кабинете.
    """

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="settings",
        verbose_name="Пользователь",
    )
    ev_notification_start = models.BooleanField(
        "Уведомлять о начале событий",
        default=False,
    )
    ev_notification_start_time = models.ManyToManyField(
        NotificationTime,
        verbose_name="Время уведомлений",
        related_name="settings",
    )
    ev_notification_new = models.BooleanField(
        "Уведомлять о новых событиях",
        default=False,
    )
    ev_type_notification = models.ManyToManyField(
        NotificationEventType,
        verbose_name="Тип события для уведомлений",
        related_name="settings",
    )
    ev_notification_method = models.ManyToManyField(
        NotificationMethod,
        verbose_name="Способ уведомления для событий",
        related_name="settings",
    )

    class Meta:
        verbose_name = "Настройки пользователя"
        verbose_name_plural = "Настройки пользователей"
        ordering = ["-pk"]

    def __str__(self):
        return str(self.pk)


class CustomUserFilter(models.Model):
    """
    Модель для фильтра пользователя в личном кабинете.
    """

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="filter",
        verbose_name="Пользователь",
    )
    is_ev_online = models.BooleanField(
        "Онлайн событие",
        default=False,
    )
    city = models.CharField(
        "Город проведения",
        max_length=FieldLength.MAX_LENGTH_CITY.value,
        blank=True,
        null=True,
    )
    specialization = models.ManyToManyField(
        Specialization,
        related_name="users_filter",
        verbose_name="Направление работы",
        blank=True,
        through="users.SpecializationsInFilter",
    )

    class Meta:
        verbose_name = "Фильтр пользователя"
        verbose_name_plural = "Фильтры пользователей"
        ordering = ["-pk"]

    def __str__(self):
        return str(self.pk)


class SpecializationsInFilter(models.Model):
    """
    Направления работы в фильтре у пользовтеля.
    У одного пользователя может быть 1 и более направлений.
    """

    filter = models.ForeignKey(
        CustomUserFilter,
        on_delete=models.CASCADE,
        related_name="specs_in_filter",
        verbose_name="Фильтр",
    )
    specialization = models.ForeignKey(
        Specialization, on_delete=models.CASCADE, verbose_name="Направления в фильтре."
    )

    class Meta:
        verbose_name = "Направления работы в фильтре"
        verbose_name_plural = "Направления работы в фильтрах"
        ordering = ["-pk"]

    def __str__(self):
        return f"{self.filter.user.email}"
