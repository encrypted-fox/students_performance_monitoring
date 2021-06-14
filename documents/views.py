import os
import mimetypes
from datetime import datetime
from django.views.generic.base import RedirectView
from openpyxl import Workbook
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.forms.models import model_to_dict
from people.models import Students
from university_structure.models import Groups
from subjects.models import Records
from django.http import HttpResponse
from shutil import make_archive
from django.shortcuts import redirect
import csv
from django.http import FileResponse
import json


import xlsxwriter

import logging

logger = logging.getLogger()

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getXLSXFromJSON(request):
    '''
    Gets xlsx document from data given. Expected input should be in format:
    {"documentData": [<number>]}, where numbers are student identificators.
    '''

    documentData = json.loads(request.query_params.get("document_data")) 
    students = Students.objects.all()
    groups = Groups.objects.all()

    if documentData:
        file_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.xlsx'
        file_path = "documents/uploads/" + file_name
        # workbook = xlsxwriter.Workbook(file_path)
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Номер", "Номер группы", "Фамилия", "Имя", "Отчество", "Email", "Средний рейтинг"])

            for element in documentData:
                current_student = students.filter(
                    id=element)[0]
                current_student_group = groups.filter(id=model_to_dict(current_student).get("group_id"))[0]
                writer.writerow([current_student.number, current_student_group.number, current_student.last_name, current_student.first_name, current_student.fathers_name, current_student.email, current_student.average_rating])
        
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = file_name
        filepath = BASE_DIR + '/documents/uploads/' + filename
        path = open(filepath, 'rb')
        from django.utils.encoding import smart_str
        mimetype, _ = mimetypes.guess_type(smart_str(file_path))
        response = HttpResponse(path, content_type=mimetype) # mimetype is replaced by content_type for django 1.7
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
        response['X-Sendfile'] = smart_str(file_path)
 
        # response = FileResponse(path)
    
        return response
    else: 
        return Response(400)


