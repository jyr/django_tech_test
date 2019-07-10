# coding: utf8
from rest_framework_guardian import filters

from urbvan_framework.views import (
    ListCreateView,
    RetrieveUpdateDestroyAPIView)

from .schemas import LocationSchema, StationSchema
from .serializers import LocationSerializer, StationSerializer
from .permissions import ObjectPermissionsEndpoint
from ..models import Location, Station

class LocationEndpoint(ListCreateView):
    """This class handles GET and POST methods."""

    queryset = Location.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer
    permission_classes = (ObjectPermissionsEndpoint,)
    filter_backends = (filters.DjangoObjectPermissionsFilter,)

class LocationDetailEndpoint(RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE methods."""

    queryset = Location.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer
    permission_classes = (ObjectPermissionsEndpoint,)
    filter_backends = (filters.DjangoObjectPermissionsFilter,)

class StationEndpoint(ListCreateView):
    """This class handles GET and POST methods."""

    queryset = Station.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer
    permission_classes = (ObjectPermissionsEndpoint,)
    filter_backends = (filters.DjangoObjectPermissionsFilter,)


class StationDetailEndpoint(RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE methods."""

    queryset = Station.objects.all()
    schema_class = StationSchema
    serializer_class = StationSerializer
    permission_classes = (ObjectPermissionsEndpoint,)
    filter_backends = (filters.DjangoObjectPermissionsFilter,)
