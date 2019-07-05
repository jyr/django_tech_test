# coding: utf8
from urbvan_framework.views import (
    ListCreateView,
    RetrieveUpdateDestroyAPIView)

from .schemas import LocationSchema, StationSchema
from .serializers import LocationSerializer, StationSerializer

from ..models import Location, Station


class LocationEndpoint(ListCreateView):

    queryset = Location.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

class LocationDetailEndpoint(RetrieveUpdateDestroyAPIView):

    queryset = Location.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer

class StationEndpoint(ListCreateView):

    queryset = Station.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer


class StationDetailEndpoint(RetrieveUpdateDestroyAPIView):

    queryset = Station.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer
