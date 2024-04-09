from enum import IntEnum


class FieldLength(IntEnum):
    """Длины полей в приложении юзеров"""

    # Атрибуты приложения Юзеров
    # Максимальная длина поля email CustomUser.email
    MAX_LENGTH_EMAIL = 254
    # Максимальная длина поля first_name CustomUser.first_name
    MAX_LENGTH_FIRST_NAME = 150
    # Максимальная длина поля last_name CustomUser.last_name
    MAX_LENGTH_LAST_NAME = 150
    # Максимальная длина поля password CustomUser.password
    MAX_LENGTH_PASSWORD = 150
    # Максимальная длина поля role CustomUser.role
    MAX_LENGTH_ROLE = 150

    # Масимальная длина поля phone CustomUser.phone
    MAX_LENGTH_PHONE = 15
    # Масимальная длина поля job CustomUserInfo.job
    MAX_LENGTH_JOB = 150
    # Масимальная длина поля experience CustomUserInfo.experience
    MAX_LENGTH_EXPERIENCE = 20
    # Масимальная длина поля specialization CustomUserInfo.specialization
    MAX_LENGTH_SPECIALIZATION = 20
    # Максимальная длина поля city CustomUserFilters.city
    MAX_LENGTH_CITY = 50
    # Максимальная длина поля slug для моделей общий
    MAX_SLUG = 50
    # Максимальная длина поля CharField для моделей общий
    MAX_NAME = 150


class ReportFieldLength(IntEnum):
    """Длины полей для модели докладов"""

    # Атрибуты модели докладов
    # Максимальная длина названия поля Report.topic
    MAX_LENGTH_TOPIC = 50
    # Максимальная длина поля Report.short_description
    MAX_LENGTH_DESCRIPTION = 500
    # Максимальная длина поля Report.speaker
    MAX_LENGTH_SPEAKER = 50
    # Максимальная длина поля Report.position
    MAX_LENGTH_POSITION = 50


class EventFieldLength(IntEnum):
    """Длины полей в приложении events"""

    MAX_LENGTH_TITLE = 100
    MAX_LENGTH_DESCRIPTION = 500
    MAX_LENGTH_CITY = 20
    MAX_LENGTH_LOCATION = 50
    MAX_LENGTH_STREAM_LINK = 200
    MAX_LENGTH_FORMAT = 7
    MAX_LENGTH_TAG = 20


# Максимальнная длина поля
# Registration.registration_stage
MAX_LENGTH_REGISTRATION_STAGE = 20

# Максимальная длина поля Notification.text
MAX_LENGTH_NOTIFICATION_TEXT = 200
