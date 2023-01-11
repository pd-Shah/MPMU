from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):

    def has_permission(self, request, view):
        # DO some calculation
        # if request.user is the owner 
        return True
