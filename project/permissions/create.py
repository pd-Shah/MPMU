from rest_framework.permissions import BasePermission

class CanCreate(BasePermission):

    def has_permission(self, request, view):
        # DO some calculation
        # if request.user could do CUD
        return True
