from rest_framework import permissions


class CheckUserCreate(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.user.user_role == 'SimpleUser':
            return False
        return True


class CheckReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'SimpleUser':
            return True
        return  False

class CheckReviewEDIT(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return  True
        return request.user == obj.user_name