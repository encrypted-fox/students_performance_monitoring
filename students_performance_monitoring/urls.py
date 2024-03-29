"""students_performance_monitoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from students_performance_monitoring.views import DocsView
from information.views import recount_average_rating, retrieve_student_records

schema_view = get_schema_view(
    openapi.Info(
        title="Students Performance Monitoring API",
        default_version='v.0.1.h',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="encrypted.fox.dev@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
urlpatterns = [
    re_path(r'^api/v0/$', DocsView.as_view()),
    re_path(r'^api/v0/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v0/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v0/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v0/admin/', admin.site.urls),
    path('api/v0/auth/', include("users.urls")),
    path('api/v0/retrieve_student_records/', retrieve_student_records),
    path('api/v0/recount_average_rating/', recount_average_rating),
    path('api/v0/', include("information.urls")),
    path('api/v0/', include("documents.urls")),
    path('api/v0/', include("subjects.urls")),
    path('api/v0/', include("people.urls")),
    path('api/v0/', include("university_structure.urls")),
    # re_path(r'^$', RedirectView.as_view(url='/front', permanent=False), name='index'),

]
