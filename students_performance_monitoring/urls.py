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
from rest_framework import routers
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.views import APIView


class DocsView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        api_docs = response = {
            "api/v0/": {
                "admin_page": request.build_absolute_uri("api/v0/admin/"),
                "university_structure": {
                    "faculties": request.build_absolute_uri("api/v0/faculties/"),
                    "educational_programs": request.build_absolute_uri("api/v0/educational_programs/"),
                    "specializations": request.build_absolute_uri("api/v0/specializations/"),
                    "groups": request.build_absolute_uri("api/v0/groups/"),
                },
                "departments": {
                    "departments": request.build_absolute_uri("api/v0/departments/"),
                    "subjects": request.build_absolute_uri("api/v0/subjects/"),
                    "subject_blocks": request.build_absolute_uri("api/v0/subject_blocks/"),
                    "subjects_subject_blocks": request.build_absolute_uri("api/v0/subjects_subject_blocks/"),
                },
                "people": {
                    "students": request.build_absolute_uri("api/v0/students/"),
                    "teachers": request.build_absolute_uri("api/v0/teachers/"),
                },
                "information": {
                    "terms": request.build_absolute_uri("api/v0/terms/"),
                    "marks": request.build_absolute_uri("api/v0/marks/"),
                    "control_types": request.build_absolute_uri("api/v0/control_types/"),
                    "records": request.build_absolute_uri("api/v0/records/"),
                },
            }
        }
        return Response(api_docs)


router = routers.DefaultRouter()
urlpatterns = [
    path('', DocsView.as_view()),
    path('api/v0/admin/', admin.site.urls),
    path('api/v0/', include("information.urls")),
    path('api/v0/', include("departments.urls")),
    path('api/v0/', include("people.urls")),
    path('api/v0/', include("university_structure.urls")),
]
