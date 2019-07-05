# coding: utf8
from rest_framework import serializers

from apps.lines.models import Line, Route


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Line
        exclude = ('id', )

class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        exclude = ('id', )
