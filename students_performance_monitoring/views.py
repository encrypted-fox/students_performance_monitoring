from builtins import staticmethod

from rest_framework.views import APIView, Response


class DocsView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        api_docs = response = {
            "api/v0/": {
                "documentation": {
                    "swagger": request.build_absolute_uri("swagger"),
                    "redoc": request.build_absolute_uri("redoc"),
                },
                "admin": request.build_absolute_uri("admin"),
                "authentication": {
                    "auth/register": request.build_absolute_uri("auth/register/"),
                    "auth/token": request.build_absolute_uri("auth/token/"),
                    "auth/token/refresh": request.build_absolute_uri("auth/token/refresh/"),
                    "auth/token/revoke": request.build_absolute_uri("auth/token/revoke/"),
                },
                "university_structure": {
                    "faculties": request.build_absolute_uri("faculties/"),
                    "educational_programs": request.build_absolute_uri("educational_programs/"),
                    "specializations": request.build_absolute_uri("specializations/"),
                    "groups": request.build_absolute_uri("groups/"),
                },
                "departments": {
                    "departments": request.build_absolute_uri("departments/"),
                    "subjects": request.build_absolute_uri("subjects/"),
                    "subject_blocks": request.build_absolute_uri("subject_blocks/"),
                    "subjects_subject_blocks": request.build_absolute_uri("subjects_subject_blocks/"),
                },
                "people": {
                    "students": request.build_absolute_uri("students/"),
                    "teachers": request.build_absolute_uri("teachers/"),
                },
                "information": {
                    "terms": request.build_absolute_uri("terms/"),
                    "marks": request.build_absolute_uri("marks/"),
                    "control_types": request.build_absolute_uri("control_types/"),
                    "records": request.build_absolute_uri("records/"),
                },
            }
        }
        return Response(api_docs)