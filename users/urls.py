from django.urls import path, include

from . import views

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('register/', views.register),
    path('token/', views.token),
    path('token/refresh/', views.refresh_token),
    path('token/revoke/', views.revoke_token),
    path('update_settings/', views.update_settings),
    path('get_user_settings/', views.get_user_settings),
]
