"""API app v.1 permissions."""


from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Permissions for request.user for editing."""
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
