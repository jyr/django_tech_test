# coding: utf8
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

class LocationDetailEndpoint(RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE methods."""

    queryset = Location.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

class StationEndpoint(ListCreateView):
    """This class handles GET and POST methods."""

    queryset = Station.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer


class StationDetailEndpoint(RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE methods."""

    queryset = Station.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer
