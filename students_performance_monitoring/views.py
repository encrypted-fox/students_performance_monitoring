from builtins import staticmethod

from rest_framework.views import APIView, Response


class DocsView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        api_docs = response = {
            "api/v0/": {
                "documentation": {
                    "swagger": request.build_absolute_uri("swagger/"),
                    "redoc": request.build_absolute_uri("redoc/"),
                },
                "admin": request.build_absolute_uri("admin/"),
                "authentication": {
                    "auth/register": request.build_absolute_uri("auth/register/"),
                    "auth/token": request.build_absolute_uri("auth/token/"),
                    "auth/token/refresh": request.build_absolute_uri("auth/token/refresh/"),
                    "auth/token/revoke": request.build_absolute_uri("auth/token/revoke/"),
                },
                "university_structure": {
                    "faculties": request.build_absolute_uri("faculties/"),
                    "departments": request.build_absolute_uri("departments/"),
                    "specializations": request.build_absolute_uri("specializations/"),
                    "education_levels": request.build_absolute_uri("education_levels/"),
                    "education_programs": request.build_absolute_uri("education_programs/"),
                    "groups": request.build_absolute_uri("groups/"),
                },
                "subjects": {
                    "subjects": request.build_absolute_uri("subjects/"),
                    "subject_blocks": request.build_absolute_uri("subject_blocks/"),
                    "subjects_subject_blocks": request.build_absolute_uri("subjects_subject_blocks/"),
                    "records": request.build_absolute_uri("records/"),
                },
                "people": {
                    "students": request.build_absolute_uri("students/"),
                    "teachers": request.build_absolute_uri("teachers/"),
                },
                "information": {
                    "start_years": request.build_absolute_uri("start_years/"),
                    "terms": request.build_absolute_uri("terms/"),
                    "marks": request.build_absolute_uri("marks/"),
                    "control_types": request.build_absolute_uri("control_types/"),           
                },
                "reports": {                         
                    'list_students_with_more_5': request.build_absolute_uri("list_students_with_more_5"),                
                    'list_students_with_more_4': request.build_absolute_uri("list_students_with_more_4"),                
                    'list_students_with_more_3': request.build_absolute_uri("list_students_with_more_3"),                
                    'list_students_with_more_2': request.build_absolute_uri("list_students_with_more_2"),                
                    'list_students_with_more_pass': request.build_absolute_uri("list_students_with_more_pass"),             
                    'list_students_with_more_not_pass': request.build_absolute_uri("list_students_with_more_not_pass"),         
                    'list_students_with_more_not_appointed': request.build_absolute_uri("list_students_with_more_not_appointed"),    
                    'list_students_only_with_more_then_2': request.build_absolute_uri("list_students_only_with_more_then_2"),      
                    'list_students_only_with_more_then_3': request.build_absolute_uri("list_students_only_with_more_then_3"),      
                    'list_students_with_less_3': request.build_absolute_uri("list_students_with_less_3"),                
                    'list_students_with_less_2': request.build_absolute_uri("list_students_with_less_2"),                
                    'list_students_with_one_3': request.build_absolute_uri("list_students_with_one_3"),                 
                    'list_students_with_one_2': request.build_absolute_uri("list_students_with_one_2"),                 
                    'list_students_with_one_pass': request.build_absolute_uri("list_students_with_one_pass"),              
                    'list_students_with_one_not_pass': request.build_absolute_uri("list_students_with_one_not_pass"),          
                    'list_students_with_one_not_appointed': request.build_absolute_uri("list_students_with_one_not_appointed"),     
                    'list_students_only_with_5': request.build_absolute_uri("list_students_only_with_5"),                
                    'list_students_only_with_4': request.build_absolute_uri("list_students_only_with_4"),                
                    'list_students_only_with_3': request.build_absolute_uri("list_students_only_with_3"),                
                    'list_students_only_with_2': request.build_absolute_uri("list_students_only_with_2"),                
                    'list_students_only_with_pass': request.build_absolute_uri("list_students_only_with_pass"),             
                    'list_students_only_with_not_pass': request.build_absolute_uri("list_students_only_with_not_pass"),         
                    'list_students_only_with_appointed': request.build_absolute_uri("list_students_only_with_appointed"),        
                    'list_students_with': request.build_absolute_uri("list_students_with"),                       
                    'list_menu_categories': request.build_absolute_uri("list_menu_categories"), 
                }
            }
        }
        return Response(api_docs)