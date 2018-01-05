from rest_framework.permissions import(
BasePermission,
SAFE_METHODS
)
from blogs.models import blogs

class IsOwner(BasePermission):
    message = 'You are not the owner of that post'
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
