from rest_framework import viewsets, permissions
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from people.models import Students, Teachers
from subjects.models import Records, SubjectBlocks, Subjects
from people.serializers import StudentsSerializer
from rest_framework.permissions import IsAuthenticated
from university_structure.models import Groups


def normalize_students(students_to_return):
    groups = Groups.objects.all()
    students_to_send = []
    for elem in students_to_return:
        dict_elem_before = model_to_dict(elem)
        dict_elem = {}
        dict_elem['id'] = dict_elem_before['id']
        dict_elem['number'] = dict_elem_before['number']
        dict_elem['group'] = model_to_dict(groups.filter(id=model_to_dict(elem)['group_id'])[0])['number']
        dict_elem['last_name'] = dict_elem_before['last_name']
        dict_elem['first_name'] = dict_elem_before['first_name']
        dict_elem['fathers_name'] = dict_elem_before['fathers_name']
        dict_elem['email'] = dict_elem_before['email']
        dict_elem['average_rating'] = dict_elem_before['average_rating']
        dict_elem['update_date'] = dict_elem_before['update_date']
        students_to_send.append(dict_elem)
    return students_to_send

def normalize_student_records(student_records):
    groups = Groups.objects.all()
    marks = Marks.objects.all()
    terms = Terms.objects.all()
    students = Students.objects.all()
    subjects = Subjects.objects.all()
    subject_blocks = SubjectBlocks.objects.all()
    teachers = Teachers.objects.all()
    control_types = ControlTypes.objects.all()
    start_years = StartYears.objects.all()

    records_to_send = []
    for elem in student_records:
        dict_elem_before = model_to_dict(elem)
        dict_elem = {}
        dict_elem['id'] = dict_elem_before['id']
        student = model_to_dict(students.filter(id=model_to_dict(elem)['student_id'])[0])
        dict_elem['student'] = student['first_name'] + " " + student['last_name']
        dict_elem['subject'] = model_to_dict(subjects.filter(id=model_to_dict(elem)['subject_id'])[0])['name']
        dict_elem['subject_block'] = model_to_dict(subject_blocks.filter(id=model_to_dict(elem)['subject_block_id'])[0])['name']
        dict_elem['group'] = model_to_dict(groups.filter(id=model_to_dict(elem)['group_id'])[0])['number']
        teacher = model_to_dict(teachers.filter(id=model_to_dict(elem)['teacher_id'])[0])
        dict_elem['teacher'] = teacher['first_name'] + " " + teacher['last_name']
        term = model_to_dict(terms.filter(id=model_to_dict(elem)['term_id'])[0])
        start_year = model_to_dict(start_years.filter(id=term['start_year_id'])[0])['year']
        dict_elem['term'] = str(term['number']) + ' семестр ' + str(start_year) + ' года'
        dict_elem['control_type'] = model_to_dict(control_types.filter(id=model_to_dict(elem)['control_type_id'])[0])['name']
        dict_elem['mark'] = model_to_dict(marks.filter(id=model_to_dict(elem)['mark_id'])[0])['name']
        dict_elem['datetime'] = dict_elem_before['datetime']
        dict_elem['retake_count'] = dict_elem_before['retake_count']
        dict_elem['is_final'] = dict_elem_before['is_final']
        records_to_send.append(dict_elem)
    return records_to_send

def filter_against_records(request):
    records = Records.objects.all()

    if 'is_final' in request.query_params:
        records = records.filter(is_final=request.query_params.get('is_final'))
    
    if 'teacher_id' in request.query_params:
        records = records.filter(teacher_id=request.query_params.get('teacher_id'))
    
    if 'group_id' in request.query_params:
        records = records.filter(group_id=request.query_params.get('group_id'))
    
    if 'subject_id' in request.query_params:
        records = records.filter(subject_id=request.query_params.get('subject_id'))
    
    if 'subject_block_id' in request.query_params:
        records = records.filter(subject_block_id=request.query_params.get('subject_block_id'))

    if 'control_type_id' in request.query_params:
        records = records.filter(control_type_id=request.query_params.get('control_type_id'))

    if 'term_id' in request.query_params:
        records = records.filter(term_id=request.query_params.get('term_id'))

    if 'mark_id' in request.query_params:
        records = records.filter(mark_id=request.query_params.get('mark_id'))

    if 'retake_count' in request.query_params:
        records = records.filter(retake_count=request.query_params.get('retake_count'))

    return records

class StartYearsViewSet(viewsets.ModelViewSet): 
    queryset = StartYears.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = StartYearsSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class TermsViewSet(viewsets.ModelViewSet):
    queryset = Terms.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TermsSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = MarksSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class ControlTypesViewSet(viewsets.ModelViewSet):
    queryset = ControlTypes.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ControlTypesSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class ListStudentsWithMore5(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_pass = marks.filter(name='Зачтено')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                else:
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_4 < counter_5:
                students_to_return.append(student)
                
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsWithMore4(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 4s then 5s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_pass = marks.filter(name='Зачтено')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                else:
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_4 > counter_5:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsWithMore3(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 4s then 5s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_3 = marks.filter(name='3')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_3 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1

                else:
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_3 > counter_4 + counter_5:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)


class ListStudentsWithMore2(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 4s then 5s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_3 = marks.filter(name='3')
        mark_id_2 = marks.filter(name='2')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')
        mark_id_not_appointed = marks.filter(name='Неявка')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_3 = 0
            counter_2 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_2[0].id):
                    counter_2 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_not_appointed[0].id):
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_2 > counter_3 + counter_4 + counter_5:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)



class ListStudentsWithMorePass(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 4s then 5s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_3 = marks.filter(name='3')
        mark_id_2 = marks.filter(name='2')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')
        mark_id_not_appointed = marks.filter(name='Неявка')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
  
            counter_pass = 0
            counter_not_pass = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_2[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_not_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_appointed[0].id):
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_pass > counter_not_pass:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)


class ListStudentsWithMoreNotPass(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 4s then 5s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_3 = marks.filter(name='3')
        mark_id_2 = marks.filter(name='2')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')
        mark_id_not_appointed = marks.filter(name='Неявка')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
  
            counter_pass = 0
            counter_not_pass = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_2[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_not_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_appointed[0].id):
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_pass < counter_not_pass:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsWithMoreNotAppointed(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 4s then 5s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_3 = marks.filter(name='3')
        mark_id_2 = marks.filter(name='2')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')
        mark_id_not_appointed = marks.filter(name='Неявка')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_3 = 0
            counter_2 = 0
            counter_pass = 0
            counter_not_pass = 0
            counter_not_appointed = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_2[0].id):
                    counter_2 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_not_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_appointed[0].id):
                    counter_not_appointed += 1
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_not_appointed > counter_5 + counter_4 + counter_3 + counter_2 + counter_pass + counter_not_pass:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsWithLess3(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 4s then 5s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_3 = marks.filter(name='3')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_3 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_3 < counter_4 + counter_5 and counter_3 > 0:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsWithLess2(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 4s then 5s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_3 = marks.filter(name='3')
        mark_id_2 = marks.filter(name='2')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')
        mark_id_not_appointed = marks.filter(name='Неявка')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_3 = 0
            counter_2 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_2[0].id):
                    counter_2 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_not_appointed[0].id):
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_2 < counter_3 + counter_4 + counter_5 and counter_2 > 0:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)
class ListStudentsOnlyWithMoreThen3(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_pass = marks.filter(name='Зачтено')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                else:
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsOnlyWithMoreThen2(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_3 = marks.filter(name='3')
        mark_id_pass = marks.filter(name='Зачтено')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_3 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1

                else:
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)


class ListStudentsWithOne5(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_2 = marks.filter(name='2')
        mark_id_3 = marks.filter(name='3')
        mark_id_4 = marks.filter(name='4')
        mark_id_5 = marks.filter(name='5')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_5 = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1

            if counter_5 == 1:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsWithOne4(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_2 = marks.filter(name='2')
        mark_id_3 = marks.filter(name='3')
        mark_id_4 = marks.filter(name='4')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_2 = 0
            counter_3 = 0
            counter_4 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_2[0].id):
                    counter_2 += 1
                    counter_all += 1

                if str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1
                
                if str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                else:
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_2 == 0 and counter_3 == 0 and counter_4 == 1:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsWithOne3(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_2 = marks.filter(name='2')
        mark_id_3 = marks.filter(name='3')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_2 = 0
            counter_3 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_2[0].id):
                    counter_2 += 1
                    counter_all += 1

                if str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

                else:
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_2 == 0 and counter_3 == 1:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)


class ListStudentsWithOne2(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_3 = marks.filter(name='3')
        mark_id_2 = marks.filter(name='2')
        mark_id_pass = marks.filter(name='Зачтено')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_3 = 0
            counter_2 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_2[0].id):
                    counter_2 += 1
                    counter_all += 1

                else:
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_2 == 1:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsWithOnePass(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_3 = marks.filter(name='3')
        mark_id_2 = marks.filter(name='2')
        mark_id_pass = marks.filter(name='Зачтено')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_3 = 0
            counter_2 = 0
            counter_pass = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_2[0].id):
                    counter_2 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_pass += 1
                    counter_all += 1

                else:
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_pass == 1:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsWithOneNotPass(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_3 = marks.filter(name='3')
        mark_id_2 = marks.filter(name='2')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')

        records = filter_against_records(request)      
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_3 = 0
            counter_2 = 0
            counter_pass = 0
            counter_not_pass = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_2[0].id):
                    counter_2 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_pass += 1
                    counter_all += 1
                
                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_not_pass += 1
                    counter_all += 1

                else:
                    counter_all += 1
                

            if counter_all == len(student_records) and len(student_records) > 0 and counter_not_pass == 1:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsWithOneNotAppointed(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_not_appointed = marks.filter(name='Неявка')

        records = filter_against_records(request)
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_not_appointed[0].id):
                    counter_all += 1

            if counter_all == 1:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)
class ListStudentsOnlyWith5(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all excellent students.
        """
        queryset = Students.objects.filter(average_rating=5.0)
        students = normalize_students(queryset)
        return Response(students)

class ListStudentsOnlyWith4(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_4 = marks.filter(name='4')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')

        records = filter_against_records(request)
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_4[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsOnlyWith3(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_3 = marks.filter(name='3')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')

        records = filter_against_records(request)
        
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_3[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsOnlyWith2(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_2 = marks.filter(name='2')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_2[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsOnlyWithPass(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_3 = marks.filter(name='3')
        mark_id_2 = marks.filter(name='2')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')
        mark_id_not_appointed = marks.filter(name='Неявка')


        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_5 = 0
            counter_4 = 0
            counter_3 = 0
            counter_2 = 0
            counter_pass = 0
            counter_not_pass = 0
            counter_not_appointed = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_2[0].id):
                    counter_2 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_not_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_appointed[0].id):
                    counter_not_appointed += 1
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_not_appointed == 0 and counter_not_pass == 0:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)


class ListStudentsOnlyWithNotPass(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_3 = marks.filter(name='3')
        mark_id_2 = marks.filter(name='2')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')
        mark_id_not_appointed = marks.filter(name='Неявка')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_5 = 0
            counter_4 = 0
            counter_3 = 0
            counter_2 = 0
            counter_pass = 0
            counter_not_pass = 0
            counter_not_appointed = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_2[0].id):
                    counter_2 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_not_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_appointed[0].id):
                    counter_not_appointed += 1
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0 and counter_not_appointed == 0 and counter_pass == 0:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)

class ListStudentsOnlyWithNotAppointed(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_not_appointed = marks.filter(name='Неявка')

        records = filter_against_records(request)
  
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if str(mark) == str(mark_id_not_appointed[0].id):
                    counter_all += 1

            if counter_all == len(student_records) and len(student_records) > 0:
                students_to_return.append(student)
        
        students_to_send = normalize_students(students_to_return)
        return Response(students_to_send)
class ListStudentsWith(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        records = filter_against_records(request)
        
        if 'student_id' in request.query_params:
            records = records.filter(student_id=request.query_params.get('student_id'))
        
       
        students = Students.objects.all()

        return Response(normalize_students(students))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recount_average_rating(request):
    students = Students.objects.all()
    records = Records.objects.filter(is_final=True)
    marks = Marks.objects.all()

    mark_id_5 = marks.filter(name='5')
    mark_id_4 = marks.filter(name='4')
    mark_id_3 = marks.filter(name='3')
    mark_id_2 = marks.filter(name='2')
    mark_id_pass = marks.filter(name='Зачтено')
    mark_id_not_pass = marks.filter(name='Незачтено')
    mark_id_not_appointed = marks.filter(name='Неявка')

    try:
        for student in students:
            student_records = records.filter(student_id=model_to_dict(student).id)
            rating_all = 0
            valuable_records_len = 0
            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['id'] 

                if (str(mark) != str(mark_id_pass[0].id) 
                    and str(mark) != str(mark_id_not_pass[0].id) 
                    and str(mark) != str(mark_id_not_appointed[0].id)):
                    rating_all += int(mark_dict['name'])
                    valuable_records_len += 1
            
            rating = rating_all / valuable_records_len
            Students.objects.filter(id=model_to_dict(student).id)[0].update(average_rating=rating)
    except:
        return Response(status=500)
    return Response(200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def retrieve_student_records(request):
    if 'id' in request.query_params:
        student = Students.objects.filter(id=request.query_params.get('id'))[0]
        records = Records.objects.filter(student_id=student.id)
        if (len(records) > 0):
            resp = normalize_student_records(records)
            return Response(resp, status=200)
        else:
            return Response([], status=204)
    return Response(status=500)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listMenuCategories(request):
    return Response([   {"id": 1, "activity": "list_students_with_more_5", "name": "Студенты с большим количеством пятерок"}, 
                        {"id": 2, "activity": "list_students_with_more_4", "name": "Студенты с большим количеством четверок"}, 
                        {"id": 3, "activity": "list_students_with_more_3", "name": "Студенты с большим количеством троек"}, 
                        {"id": 4, "activity": "list_students_with_more_2", "name": "Студенты с большим количеством двоек"}, 
                        {"id": 5, "activity": "list_students_with_more_pass", "name": "Студенты с большим количеством оценок зачтено"},
                        {"id": 6, "activity": "list_students_with_more_not_pass", "name": "Студенты с большим количеством оценок незачтено"},
                        {"id": 7, "activity": "list_students_with_more_not_appointed", "name": "Студенты с большим количеством неявок"},
                        {"id": 8, "activity": "list_students_only_with_more_then_3", "name": "Студенты со всеми оценками больше тройки"}, 
                        {"id": 9, "activity": "list_students_only_with_more_then_2", "name": "Студенты со всеми оценками больше двойки"}, 
                        {"id": 10, "activity": "list_students_with_less_3", "name": "Студенты с меньшим количеством троек"}, 
                        {"id": 11, "activity": "list_students_with_less_2", "name": "Студенты с меньшим количеством двоек"}, 
                        # {"id": 12, "activity": "list_students_with_one_5", "name": "Студенты с одной пятеркой"}, 
                        # {"id": 13, "activity": "list_students_with_one_4", "name": "Студенты с одной четверкой"}, 
                        # {"id": 14, "activity": "list_students_with_one_3", "name": "Студенты с одной тройкой"}, 
                        # {"id": 15, "activity": "list_students_with_one_2", "name": "Студенты с одной двойкой"}, 
                        # {"id": 16, "activity": "list_students_with_one_not_pass", "name": "Студенты с одним незачетом"}, 
                        # {"id": 17, "activity": "list_students_with_one_pass", "name": "Студенты с одним зачетом"}, 
                        # {"id": 12, "activity": "list_students_with_one_not_appointed", "name": "Студенты с одной неявкой"}, 
                        {"id": 12, "activity": "list_students_only_with_5", "name": "Студенты только с пятерками"}, 
                        {"id": 13, "activity": "list_students_only_with_4", "name": "Студенты только с четверками"}, 
                        {"id": 14, "activity": "list_students_only_with_3", "name": "Студенты только с тройками"}, 
                        {"id": 15, "activity": "list_students_only_with_2", "name": "Студенты только с двойками"}, 
                        {"id": 16, "activity": "list_students_only_with_pass", "name": "Студенты только с оценками зачтено"}, 
                        {"id": 17, "activity": "list_students_only_with_not_pass", "name": "Студенты только с оценками незачтено"}, 
                        {"id": 18, "activity": "list_students_only_with_not_appointed", "name": "Студенты только с неявками"}, 
                        {"id": 19, "activity": "list_students_with", "name": "Найти студентов по запросу"}, 
                     ])
                     