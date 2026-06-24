from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.account.api_views import (
    EmployeeTokenObtainPairView,
    EmployerTokenObtainPairView,
    MeView,
)

urlpatterns = [
    path('api/auth/token/employee/', EmployeeTokenObtainPairView.as_view(), name='jwt-token-employee'),
    path('api/auth/token/employer/', EmployerTokenObtainPairView.as_view(), name='jwt-token-employer'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='jwt-token-refresh'),
    path('api/auth/me/', MeView.as_view(), name='jwt-me'),
]

