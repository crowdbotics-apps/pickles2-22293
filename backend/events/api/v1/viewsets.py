from rest_framework import authentication
from events.models import Event, Location
from .serializers import EventSerializer, LocationSerializer
from rest_framework import viewsets


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Event.objects.all()


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Location.objects.all()
