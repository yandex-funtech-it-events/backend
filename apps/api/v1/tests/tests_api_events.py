from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import CustomUser
from apps.events.models import EventTags


class EventTagsTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(
            username="test_user",
            email="user@mail.ru",
            password="test_user_password",
            phone="1234",
        )
        self.token = RefreshToken.for_user(self.user)
        self.simple_client = APIClient()
        self.simple_client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token.access_token}"
        )
        self.tag = EventTags.objects.create(name="Test tag")

    def test_event_tags_retrieve(self):
        response = self.simple_client.get("/api/v1/tags/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_tags_create(self):
        response = self.simple_client.post("/api/v1/tags/")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
