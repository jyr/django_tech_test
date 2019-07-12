# coding: utf8
from datetime import datetime
from uuid import uuid4

from django.contrib.auth import get_permission_codename
from django.conf import settings

from guardian.shortcuts import assign_perm

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

def add_permissions(group, object):
    actions = ['add', 'change', 'delete', 'view']
    for action in actions:
        codename = get_permission_codename(action, object._meta)
        assign_perm(codename, group, object)

def is_owner(obj, request):
    return obj.owner == request.user
