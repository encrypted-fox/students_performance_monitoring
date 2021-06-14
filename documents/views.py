from datetime import datetime

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.forms.models import model_to_dict
from people.models import Students
from university_structure.models import Groups
from subjects.models import Records

import xlsxwriter

import logging

logger = logging.getLogger()

# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def getXLSXFromJSON(request):
    documentData = request.data.get('documentData', None)
    userId = request.data.get('userId', None)
    students = Students.objects.all()
    groups = Groups.objects.all()

    if documentData and userId:
        workbook = xlsxwriter.Workbook(
            str(userId) + "-" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.xlsx')
        worksheet = workbook.add_worksheet()


        worksheet.set_column('A:A', 20)
        worksheet.set_column('B:B', 15)
        worksheet.set_column('C:E', 15)
        worksheet.set_column('F:F', 25)
        worksheet.set_column('G:G', 15)



        # Add a bold format to use to highlight cells.
        bold = workbook.add_format({'bold': True})

        col = 0
        row = 0

        worksheet.write(row, col, "Номер", bold)
        col += 1
        worksheet.write(row, col, "Номер группы", bold)
        col += 1
        worksheet.write(row, col, "Фамилия", bold)
        col += 1
        worksheet.write(row, col, "Имя", bold)
        col += 1
        worksheet.write(row, col, "Отчество", bold)
        col += 1
        worksheet.write(row, col, "Email", bold)
        col += 1
        worksheet.write(row, col, "Средний рейтинг", bold)

        col = 0
        row += 1

        for element in documentData:
            current_student = students.filter(
                id=element)[0]
            current_student_group = groups.filter(id=model_to_dict(current_student).get("group_id"))[0]
            logger.log(1, current_student_group)

            worksheet.write(row, col, current_student.number)
            col += 1
            worksheet.write(row, col, current_student_group.number)
            col += 1
            worksheet.write(row, col, current_student.last_name)
            col += 1
            worksheet.write(row, col, current_student.first_name)
            col += 1
            worksheet.write(row, col, current_student.fathers_name)
            col += 1
            worksheet.write(row, col, current_student.email)
            col += 1
            worksheet.write(
                row, col, current_student.average_rating)

            col = 0
            row += 1

        workbook.close()
        return Response(200)
    else: 
        return Response(400)


