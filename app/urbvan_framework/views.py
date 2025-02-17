# coding: utf8
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from .mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
    )
from .schemas import PaginationResponse
from .authentication import CustomTokenAuthentication
from urbvan.permissions import ObjectPermissionsEndpoint, IsOwnerOrReadOnly


class CreateAPIView(CreateModelMixin, GenericAPIView):
    """
    Concrete view for creating a model instance.
    """
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
        ObjectPermissionsEndpoint,
        IsOwnerOrReadOnly
    )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListAPIView(ListModelMixin, GenericAPIView):
    """
    Concrete view for listing a queryset.
    """

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
        ObjectPermissionsEndpoint,
        IsOwnerOrReadOnly
    )

    pagination_class = PaginationResponse

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RetrieveUpdateDestroyAPIView(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericAPIView):
    """
    Concrete view for retrieving a model instance
    """

    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
        ObjectPermissionsEndpoint,
        IsOwnerOrReadOnly
    )

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ListCreateView(CreateAPIView, ListAPIView):
    pass
