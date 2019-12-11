from django.urls import path, include

from .api import RegisterAPI, TokenAPI, RefreshTokenAPI, RevokeTokenAPI

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', TokenAPI.as_view()),
    path('auth/refresh', RefreshTokenAPI.as_view()),
    path('auth/revoke', RevokeTokenAPI.as_view()),
]
