import datetime

from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from apps.events.choice_classes import FormatChoices
from apps.events.models import Events, EventTags, Registration
from apps.users.choice_classes import RoleChoices
from apps.users.models import CustomUser


class EventTagsTestCase(APITestCase):
    """Тесты api для тэгов мероприятия"""

    def setUp(self):
        self.simple_user = CustomUser.objects.create(
            username="test_user",
            email="user@mail.ru",
            password="test_user_password",
            phone="1234",
        )
        self.simple_user_token = RefreshToken.for_user(self.simple_user)
        self.simple_client = APIClient()
        self.simple_client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.simple_user_token.access_token}"
        )

        self.organizer_user = CustomUser.objects.create(
            username="test_organizer",
            email="organizer@mail.ru",
            password="test_organizer_password",
            phone="12345",
            role=RoleChoices.ORGANIZER,
        )
        self.organizer_token = RefreshToken.for_user(self.organizer_user)
        self.organizer_client = APIClient()
        self.organizer_client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.organizer_token.access_token}"
        )

        self.tag = EventTags.objects.create(name="Test tag")

    # Тест на получение списка тэгов
    def test_event_tags_list(self):
        response = self.simple_client.get("/api/v1/tags/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Тест на создание тэга
    def test_event_tags_create(self):
        response = self.simple_client.post("/api/v1/tags/", {"name": "new tag"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Тест на удаление тэга
    def test_event_tags_delete(self):
        response = self.simple_client.delete(f"/api/v1/tags/{self.tag.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.organizer_client.delete(f"/api/v1/tags/{self.tag.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class EventsTestCase(APITestCase):
    """Тесты api для мероприятий"""

    def setUp(self):
        self.simple_user = CustomUser.objects.create(
            username="test_user",
            email="user@mail.ru",
            password="test_user_password",
            phone="1234",
        )
        self.simple_user_token = RefreshToken.for_user(self.simple_user)
        self.simple_client = APIClient()
        self.simple_client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.simple_user_token.access_token}"
        )

        self.organizer_user = CustomUser.objects.create(
            username="test_organizer",
            email="organizer@mail.ru",
            password="test_organizer_password",
            phone="12345",
            role=RoleChoices.ORGANIZER,
        )
        self.organizer_token = RefreshToken.for_user(self.organizer_user)
        self.organizer_client = APIClient()
        self.organizer_client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.organizer_token.access_token}"
        )

        self.tag = EventTags.objects.create(name="Test tag")
        self.event = Events.objects.create(
            title="test_title",
            description="test_description",
            format=FormatChoices.ONLINE,
            creator=self.organizer_user,
            moderator=self.organizer_user,
            registration_open=timezone.now(),
            registration_close=timezone.now(),
            date_start=datetime.date.today(),
            date_end=datetime.date.today(),
        )
        self.event.tags.add(self.tag)
        self.registration = Registration.objects.create(
            event=self.event,
            user=self.simple_user,
        )

    # Тест на получение списка мероприятий
    def test_event_list(self):
        response = self.simple_client.get("/api/v1/events/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Тест на создание мероприятия
    def test_event_create(self):
        response = self.simple_client.post(
            "/api/v1/events/",
            {
                "title": "new event",
                "description": "new description",
                "format": FormatChoices.ONLINE,
                "creator": self.organizer_user.id,
                "moderator": self.organizer_user.id,
                "tags": [{"id": self.tag.id, "name": "Test tag"}],
                "registration_open": timezone.now(),
                "registration_close": timezone.now(),
                "date_start": datetime.date.today(),
                "date_end": datetime.date.today(),
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Тест на удаление мероприятия
    def test_event_delete(self):
        response = self.simple_client.delete(f"/api/v1/events/{self.event.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.organizer_client.delete(f"/api/v1/events/{self.event.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Тест на регистрацию на мероприятие
    def test_event_register(self):
        response = self.simple_client.post(f"/api/v1/events/{self.event.id}/register/")
        if self.event.registration_close > timezone.now():
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Тест на отмену регистрации
    def test_event_unregister(self):
        response = self.simple_client.post(
            f"/api/v1/events/{self.event.id}/unregister/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
