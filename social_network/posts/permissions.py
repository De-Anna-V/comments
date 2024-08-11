from rest_framework.permissions import BasePermission

class Allowed(BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method == 'GET':
            return True
        return request.user == object.user