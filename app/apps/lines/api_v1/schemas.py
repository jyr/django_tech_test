# coding: utf8
from marshmallow import (Schema, fields)

from apps.stations.api_v1.schemas import StationSchema

class LineSchema(Schema):

    id = fields.String()
    model = fields.String()
    color = fields.String()

class RouteSchema(Schema):
    id = fields.String()
    line = fields.Nested(LineSchema)
    station = fields.Nested(StationSchema, many=True)
    direction = fields.Boolean()
    is_active = fields.Boolean()
