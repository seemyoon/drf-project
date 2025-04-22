from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.is_superuser)
    # return only one method has_permission, which check if we have user (request.user) and if user is_staff/is_superuser (request.user.is_staff, request.user.is_superuser)