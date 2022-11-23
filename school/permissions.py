
from rest_framework.permissions import BasePermission,AllowAny


class IsAdminUser_ForAdmin(BasePermission):
    def has_permission(self, request,view):
        # import pdb;pdb.set_trace()
        return bool(
            request.user and request.user.is_staff and request.user.is_superuser
        )


# class ActionBasedPermission(AllowAny):
#     """
#     Grant or deny access to a view, based on a mapping in view.action_permissions
#     """
#     def has_permission(self, request, view):
#         for klass, actions in getattr(view, 'action_permissions', {}).items():
#             if view.action in actions:
#                 return klass().has_permission(request, view)
#         return False