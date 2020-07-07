from builtins import staticmethod

from rest_framework.views import APIView, Response


class DocsView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        api_docs = response = {
            "api/v0/": {
                "documentation": {
                    "swagger": request.build_absolute_uri("api/v0/swagger"),
                    "redoc": request.build_absolute_uri("api/v0/redoc"),
                },
                "admin": request.build_absolute_uri("api/v0/admin"),
                "authentication": {
                    "auth/register": request.build_absolute_uri("api/v0/auth/register/"),
                    "auth/token": request.build_absolute_uri("api/v0/auth/token/"),
                    "auth/token/refresh": request.build_absolute_uri("api/v0/auth/token/refresh/"),
                    "auth/token/revoke": request.build_absolute_uri("api/v0/auth/token/revoke/"),
                },
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