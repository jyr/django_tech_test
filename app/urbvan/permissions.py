import logging

from django.contrib.auth.models import User

from rest_framework import permissions

from guardian.core import ObjectPermissionChecker

from apps.stations.models import Location
from apps.utils import is_owner

class ObjectPermissionsEndpoint(permissions.DjangoObjectPermissions):

    def has_permission(self, request, view):

        if (request.method in permissions.SAFE_METHODS and
            request.user.is_authenticated):
            return True

        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.is_authenticated

        return False


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.        
        if (request.method in permissions.SAFE_METHODS
            and is_owner(obj, request)):
            return True

        checker = ObjectPermissionChecker(request.user)
        if checker.has_perm('view_location', obj.id):
            return True

        return False
