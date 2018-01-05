from rest_framework.permissions import(
BasePermission,
SAFE_METHODS
)
from blogs.models import blogs

class IsOwner(BasePermission):
    message = 'You are not allowed to do that'
    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsLogged(BasePermission):
    message = "You are not logged in"

    def has_permission(self, request, view):
        if request.user.is_authenticated():
            return True
        else:
            return False
