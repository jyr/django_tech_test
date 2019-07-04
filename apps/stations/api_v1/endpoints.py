# coding: utf8
from urbvan_framework.views import ListCreateView

from .schemas import LocationSchema
from .serializers import LocationSerializer

from ..models import Location


class LocationView(ListCreateView):

    queryset = Location.objects.all()
    schema_class = LocationSchema
    serializer_class = LocationSerializer
