from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView

User = get_user_model()


class RoleRestrictedTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Validate user credentials + required role (employee/employer)."""

    required_role: str | None = None

    @classmethod
    def get_token(cls, user):  # noqa: N805
        token = super().get_token(user)
        token['role'] = user.role
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        # super().validate sets self.user
        user = getattr(self, 'user', None)
        if self.required_role and user and user.role != self.required_role:
            raise self.get_serializer_error(
                {
                    'detail': f'User role must be {self.required_role} to access this endpoint.'
                }
            )
        return data


class EmployeeTokenObtainPairSerializer(RoleRestrictedTokenObtainPairSerializer):
    required_role = 'employee'


class EmployerTokenObtainPairSerializer(RoleRestrictedTokenObtainPairSerializer):
    required_role = 'employer'


class EmployeeTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmployeeTokenObtainPairSerializer


class EmployerTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmployerTokenObtainPairSerializer


class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(
            {
                'id': request.user.id,
                'email': request.user.email,
                'role': request.user.role,
                'gender': request.user.gender,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
            },
            status=status.HTTP_200_OK,
        )

