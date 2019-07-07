# coding: utf8
from datetime import datetime
from uuid import uuid4

from django.conf import settings

def create_id(identifier):
    id_base = "{}{}{}{}{}{}{}{}"
    now = datetime.utcnow()
    id_base = id_base.format(
        identifier,
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second,
        str(uuid4())[:8]
    )
    return id_base

def tenant_db_from_request(request):
    # ToDo Refactor
    method = request.method
    if settings.DJANGO_ENV == 'test':
        return "default"
    else:
        map = methods_map()
        db = map.get(method)

    return db

def methods_map():
    # ToDo Refactor
    return {
        "GET": "read",
        "POST": "write",
        "PUT": "write",
        "PATCH": "write",
        "DELETE": "write"
    }
