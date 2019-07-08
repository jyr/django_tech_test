from urbvan_framework.views import (
    ListCreateView,
    RetrieveUpdateDestroyAPIView)

from .schemas import LineSchema, RouteSchema
from .serializers import LineSerializer, RouteSerializer

from ..models import Line, Route

class LineEndpoint(ListCreateView):

    queryset = Line.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer

class LineDetailEndpoint(RetrieveUpdateDestroyAPIView):

    queryset = Line.objects.all()
    schema_class = LineSchema
    serializer_class = LineSerializer

class RouteEndpoint(ListCreateView):

    queryset = Route.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer

class RouteDetailEndpoint(RetrieveUpdateDestroyAPIView):

    queryset = Route.objects.all()
    schema_class = RouteSchema
    serializer_class = RouteSerializer
