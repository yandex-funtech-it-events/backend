from enum import IntEnum


class FieldLength(IntEnum):
    """Длины полей в приложении юзеров"""

    # Атрибуты приложения Юзеров
    # Максимальная длина поля email User.email
    MAX_LENGTH_EMAIL = 254
    # Максимальная длина поля first_name User.first_name
    MAX_LENGTH_FIRST_NAME = 150
    # Максимальная длина поля last_name User.last_name
    MAX_LENGTH_LAST_NAME = 150
    # Максимальная длина поля password User.password
    MAX_LENGTH_PASSWORD = 150
    # Максимальная длина поля role User.role
    MAX_LENGTH_ROLE = 150


class EventFieldLength(IntEnum):
    """Длины полей в приложении events"""

    MAX_LENGTH_TITLE = 100
    MAX_LENGTH_DESCRIPTION = 500
    MAX_LENGTH_CITY = 20
    MAX_LENGTH_LOCATION = 50
    MAX_LENGTH_STREAM_LINK = 200
    MAX_LENGTH_FORMAT = 7
    MAX_LENGTH_TAG = 20
