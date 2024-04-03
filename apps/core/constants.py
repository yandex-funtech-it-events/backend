from enum import IntEnum


class FieldLenght(IntEnum):
    """Длины полей в приложении юзеров"""

    # Атрибуты приложения Юзеров
    # Максимальная длина поля email User.email
    MAX_LENGHT_EMAIL = 254
    # Максимальная длина поля first_name User.first_name
    MAX_LENGHT_FIRST_NAME = 150
    # Максимальная длина поля last_name User.last_name
    MAX_LENGHT_LAST_NAME = 150
    # Максимальная длина поля password User.password
    MAX_LENGHT_PASSWORD = 150
    # Максимальная длина поля role User.role
    MAX_LENGHT_ROLE = 150
