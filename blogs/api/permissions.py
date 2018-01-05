from rest_framework.permissions import(
BasePermission,
SAFE_METHODS
)

class IsSuperUser(BasePermission):
    message = "You are not the owner of this blog"
    my_safe_method = ['GET','PUT']

    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        return False
    #this is to ensure it's for getting or updating purpose only

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser
