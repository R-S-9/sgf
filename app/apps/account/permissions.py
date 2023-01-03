from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    """Права на отправку данных, только для пользователей, не гостей"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user
