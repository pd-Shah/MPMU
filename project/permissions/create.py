from rest_framework.permissions import BasePermission

class CanCreate(BasePermission):

    def has_permission(self, request, view):
        return True
