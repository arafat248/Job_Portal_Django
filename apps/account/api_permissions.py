from rest_framework import permissions


class RolePermission(permissions.BasePermission):
    required_role: str = ''

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == self.required_role)

