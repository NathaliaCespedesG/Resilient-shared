from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsHealthcareProfessional(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'healthcare_professional'

class IsParticipant(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'participant'