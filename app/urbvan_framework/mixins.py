# coding: utf8
from django.shortcuts import get_object_or_404 as _get_object_or_404

from rest_framework import (mixins, status)
from rest_framework.response import Response

from .utils import (render_to_response, render_response_error)

from apps.stations.models import Location

class CreateModelMixin(mixins.CreateModelMixin):
    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            response = render_response_error(errors=serializer.errors)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        try:
            self.perform_create(serializer)
        except Exception as e:
            if hasattr(e, 'detail'):
                error = e.detail
            else:
                error = {"base": {"message": str(e)}}

            response = render_response_error(errors=error)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        instance = serializer.instance

        schema = self.schema_class()
        schema = schema.dump(instance).data

        response = render_to_response(body=schema)

        return Response(response, status=status.HTTP_201_CREATED)


class ListModelMixin(object):
    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        schema = self.schema_class(many=True)
        schema = schema.dump(page).data

        return self.get_paginated_response(schema)

class RetrieveModelMixin(object):
    """
    Retrieve a model instance.
    """

    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()

        schema = self.schema_class()
        schema = schema.dump(instance).data

        response = render_to_response(body=schema)

        return Response(response)

class UpdateModelMixin(object):
    """
    Update a model instance.
    """

    def update(self, request, *args, **kwargs):
        #print(kwargs, flush=True)
        #print(self, flush=True)
        partial = kwargs.pop('partial', False)
        instance = _get_object_or_404(Location, pk=kwargs["pk"])

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        schema = self.schema_class()
        schema = schema.dump(instance).data
        response = render_to_response(body=schema)

        return Response(response)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class DestroyModelMixin(object):
    """
    Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        instance = _get_object_or_404(Location, pk=kwargs["pk"])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
