from rest_framework import viewsets, permissions, authentication, generics
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from people.models import Students
from subjects.models import Records
from people.serializers import StudentsSerializer
import logging

logger = logging.getLogger()


class StartYearsViewSet(viewsets.ModelViewSet):
    queryset = StartYears.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StartYearsSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class TermsViewSet(viewsets.ModelViewSet):
    queryset = Terms.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TermsSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MarksSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class ControlTypesViewSet(viewsets.ModelViewSet):
    queryset = ControlTypes.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ControlTypesSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class ListStudentsWithMore5(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        logger.error(request.query_params)

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_pass = marks.filter(name='Зачтено')

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
        
        else:
            records = Records.objects.all()
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['name'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

            if counter_all == len(student_records) and counter_4 < counter_5:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

class ListStudentsWithMore4(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students with more 4s then 5s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_pass = marks.filter(name='Зачтено')

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
        
        else:
            records = Records.objects.all()
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['name'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

            if counter_all == len(student_records) and counter_4 > counter_5:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

class ListStudentsWithMore4(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students with more 4s then 5s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_pass = marks.filter(name='Зачтено')

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
        
        else:
            records = Records.objects.all()
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['name'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

            if counter_all == len(student_records) and counter_4 > counter_5:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

class ListStudentsWithMore3(viewsets.ViewSet):

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
        
        else:
            records = Records.objects.all()
       
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
                mark = mark_dict['name'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_all += 1

            if counter_all == len(student_records) and counter_3 > counter_4 + counter_5:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)


class ListStudentsWithMore2(viewsets.ViewSet):

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
        
        else:
            records = Records.objects.all()
       
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
                mark = mark_dict['name'] 

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

            if counter_all == len(student_records) and counter_2 > counter_3 + counter_4 + counter_5:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

class ListStudentsWithLess3(viewsets.ViewSet):

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
        
        else:
            records = Records.objects.all()
       
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
                mark = mark_dict['name'] 

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

            if counter_all == len(student_records) and counter_3 < counter_4 + counter_5 and counter_3 > 0:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

class ListStudentsWithLess2(viewsets.ViewSet):
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
        
        else:
            records = Records.objects.all()
       
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
                mark = mark_dict['name'] 

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

            if counter_all == len(student_records) and counter_2 < counter_3 + counter_4 + counter_5:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)
class ListStudentsOnlyWithMoreThen3(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_pass = marks.filter(name='Зачтено')

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
        
        else:
            records = Records.objects.all()
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['name'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

            if counter_all == len(student_records):
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

class ListStudentsOnlyWithMoreThen2(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_3 = marks.filter(name='3')
        mark_id_pass = marks.filter(name='Зачтено')

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
        
        else:
            records = Records.objects.all()
       
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
                mark = mark_dict['name'] 

                if str(mark) == str(mark_id_5[0].id):
                    counter_5 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_4[0].id):
                    counter_4 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

            if counter_all == len(student_records):
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

class ListStudentsWithOne3(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_2 = marks.filter(name='2')
        mark_id_3 = marks.filter(name='3')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')

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
        
        else:
            records = Records.objects.all()
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_2 = 0
            counter_3 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['name'] 

                if str(mark) == str(mark_id_2[0].id):
                    counter_2 += 1
                    counter_all += 1

                if str(mark) == str(mark_id_3[0].id):
                    counter_3 += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_all += 1

            if counter_all == len(student_records) and counter_2 == 0 and counter_3 == 1:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

class ListStudentsWithOne2(viewsets.ViewSet):

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
        
        else:
            records = Records.objects.all()
       
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
                mark = mark_dict['name'] 

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

            if counter_all == len(student_records) and counter_2 == 1:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

class ListStudentsWithOneNotAppointed(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_not_appointed = marks.filter(name='Неявка')

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
        
        else:
            records = Records.objects.all()
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['name'] 

                if str(mark) == str(mark_id_not_appointed[0].id):
                    counter_all += 1

            if counter_all == 1:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)
class ListStudentsOnlyWith5(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all excellent students.
        """
        queryset = Students.objects.filter(average_rating=5.0)
        serializer = StudentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

class ListStudentsOnlyWith4(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_4 = marks.filter(name='4')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')

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
        
        else:
            records = Records.objects.all()
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['name'] 

                if str(mark) == str(mark_id_4[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_all += 1

            if counter_all == len(student_records):
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

class ListStudentsOnlyWith3(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_3 = marks.filter(name='3')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')

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
        
        else:
            records = Records.objects.all()
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['name'] 

                if str(mark) == str(mark_id_3[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_all += 1

            if counter_all == len(student_records):
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

class ListStudentsOnlyWith2(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_2 = marks.filter(name='2')
        mark_id_pass = marks.filter(name='Зачтено')
        mark_id_not_pass = marks.filter(name='Незачтено')

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
        
        else:
            records = Records.objects.all()
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['name'] 

                if str(mark) == str(mark_id_2[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_pass[0].id):
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_all += 1

            if counter_all == len(student_records):
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

class ListStudentsOnlyWithNotAppointed(viewsets.ViewSet):
    
    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        marks = Marks.objects.all()

        mark_id_not_appointed = marks.filter(name='Неявка')

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
        
        else:
            records = Records.objects.all()
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(record.mark_id) 
                mark = mark_dict['name'] 

                if str(mark) == str(mark_id_not_appointed[0].id):
                    counter_all += 1

            if counter_all == len(student_records):
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)
class ListStudentsWith(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """

        records = Records.objects.all()

        if 'student_id' in request.query_params:
            records = records.filter(student_id=request.query_params.get('student_id'))

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
        
        else:
            records = Records.objects.all()
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            if len(student_records) > 0:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

