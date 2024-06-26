from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.api.v1.events.permissions import IsOrganizerOrReadOnly
from apps.api.v1.events.serializers import (
    EventsSerializer,
    EventTagsSerializer,
    FavoritesSerializers,
    RegistrationSerializer,
    ReportSerializer,
)
from apps.events.choice_classes import RegistrationStageChoices
from apps.events.models import Events, EventTags, Favorites, Registration, Report


class EventTagsViewSet(viewsets.ModelViewSet):
    """Обработчик запросов на эндпоинты EventTags"""

    queryset = EventTags.objects.all()
    serializer_class = EventTagsSerializer

    def get_permissions(self):
        if self.action in ["list", "create"]:
            return [IsAuthenticated()]
        elif self.action in ["partial_update", "destroy"]:
            return [IsOrganizerOrReadOnly()]
        else:
            return [AllowAny()]


class EventsViewSet(viewsets.ModelViewSet):
    """Обработчик запросов на эндпоинты Events"""

    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def get_permissions(self):
        if self.action in ["list", "create"]:
            return [IsAuthenticated()]
        elif self.action in ["partial_update", "destroy"]:
            return [IsOrganizerOrReadOnly()]
        else:
            return [AllowAny()]

    @action(
        detail=True,
        methods=[
            "POST",
        ],
        permission_classes=(IsAuthenticated,),
    )
    def register(self, request, *args, **kwargs):
        event = get_object_or_404(Events, id=kwargs["pk"])
        if Registration.objects.filter(event=event, user=request.user).exists():
            return Response(
                {"error": "Вы уже зарегистрированы на мероприятие"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if event.registration_close < timezone.now():
            return Response(
                {"error": "Регистрация на мероприятия закрыта"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Registration.objects.create(
            user=request.user,
            event=event,
            registration_stage=RegistrationStageChoices.PARTICIPATING,
        )

        return Response(
            {"message": "Регистрация успешно создана"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(
        detail=True,
        methods=[
            "POST",
        ],
        permission_classes=(IsAuthenticated,),
    )
    def unregister(self, request, *args, **kwargs):
        event = get_object_or_404(Events, id=kwargs["pk"])
        if Registration.objects.filter(event=event, user=request.user).exists():
            Registration.objects.filter(event=event, user=request.user).delete()

            return Response(
                {"message": "Регистрация успешно отменена"},
                status=status.HTTP_204_NO_CONTENT,
            )

    @action(
        detail=True,
        methods=[
            "GET",
        ],
        permission_classes=(IsOrganizerOrReadOnly,),
    )
    def registrations(self, request, *args, **kwargs):
        event = get_object_or_404(Events, id=kwargs["pk"])
        if Registration.objects.filter(event=event).exists():
            registrations = Registration.objects.filter(
                event=event,
            )

            serializer = RegistrationSerializer(
                registrations,
                context={"request": request},
                many=True,
            )
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)


class ReportViewSet(viewsets.ModelViewSet):
    """Обработчик запросов на эндпойнты Report"""

    serializer_class = ReportSerializer
    permission_classes = (
        IsOrganizerOrReadOnly,
        IsAuthenticated,
    )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["event_id"] = self.kwargs.get("event_id", None)
        return context

    def get_queryset(self):
        queryset = Report.objects.filter(event=self.kwargs.get("event_id", None))
        return queryset


class FavoritesViewSet(viewsets.ModelViewSet):
    """Обработчик запросов на эндпоинты Favorites"""

    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializers

    @action(detail=True, methods=["post"])
    def add_event_to_favorites(self, request, pk=None):
        event_id = request.data("event_id")
        favorite = self.get.object()
        favorite.events.add(event_id)
        favorite.save()
        return Response(
            {"message: Event added to favorites"}, status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["delete"])
    def rm_event_from_favorites(self, request, pk=None):
        event_id = request.data("event_id")
        favorite = self.get.object()
        favorite.events.remove(event_id)
        favorite.save()
        return Response(
            {"message: Successfully removed from favorites"}, status=status.HTTP_200_OK
        )
