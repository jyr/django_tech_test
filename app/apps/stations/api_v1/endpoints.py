# coding: utf8
from rest_framework_guardian import filters
from rest_framework import permissions

from urbvan_framework.views import (
    ListCreateView,
    RetrieveUpdateDestroyAPIView)

from .schemas import LocationSchema, StationSchema
from .serializers import LocationSerializer, StationSerializer

from ..models import Location, Station

class LocationEndpoint(ListCreateView):
    """This class handles GET and POST methods."""

    queryset = Location.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer
    model_class = Location

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LocationDetailEndpoint(RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE methods."""

    queryset = Location.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer
    model_class = Location

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StationEndpoint(ListCreateView):
    """This class handles GET and POST methods."""

    queryset = Station.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer
    model_class = Station

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StationDetailEndpoint(RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE methods."""

    queryset = Station.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer
    model_class = Station
