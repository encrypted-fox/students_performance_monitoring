from rest_framework import viewsets, permissions
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from people.models import Students
from subjects.models import Records
from people.serializers import StudentsSerializer
from rest_framework.permissions import IsAuthenticated


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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_3 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name'] 
                

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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
  
            counter_pass = 0
            counter_not_pass = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
                mark = mark_dict['name'] 

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

            if counter_all == len(student_records) and counter_pass > counter_not_pass:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)


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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
  
            counter_pass = 0
            counter_not_pass = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
                mark = mark_dict['name'] 

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

            if counter_all == len(student_records) and counter_pass < counter_not_pass:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

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
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
                    counter_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_not_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_appointed[0].id):
                    counter_not_appointed += 1
                    counter_all += 1

            if counter_all == len(student_records) and counter_not_appointed > counter_5 + counter_4 + counter_3 + counter_2 + counter_pass + counter_not_pass:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_3 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_5 = 0
            counter_4 = 0
            counter_3 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_2 = 0
            counter_3 = 0
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
                    counter_pass += 1
                    counter_all += 1

            if counter_all == len(student_records) and counter_pass == 1:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

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
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
                    counter_pass += 1
                    counter_all += 1
                
                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_not_pass += 1
                    counter_all += 1
                

            if counter_all == len(student_records) and counter_not_pass == 1:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
                mark = mark_dict['name'] 

                if str(mark) == str(mark_id_not_appointed[0].id):
                    counter_all += 1

            if counter_all == 1:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)
class ListStudentsOnlyWith5(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def list(self, request):
        """
        This view should return a list of all excellent students.
        """
        queryset = Students.objects.filter(average_rating=5.0)
        serializer = StudentsSerializer(queryset, many=True)
        return Response(serializer.data)

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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
                    counter_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_not_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_appointed[0].id):
                    counter_not_appointed += 1
                    counter_all += 1

            if counter_all == len(student_records) and counter_not_appointed == 0 and counter_not_pass == 0:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)


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
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
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
                    counter_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_pass[0].id):
                    counter_not_pass += 1
                    counter_all += 1

                elif str(mark) == str(mark_id_not_appointed[0].id):
                    counter_not_appointed += 1
                    counter_all += 1

            if counter_all == len(student_records) and counter_not_appointed == 0 and counter_pass == 0:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)
            
            counter_all = 0

            for record in student_records:
                mark_dict = model_to_dict(marks.filter(id=record.mark_id)) 
                mark= mark_dict['name']  
                mark = mark_dict['name'] 

                if str(mark) == str(mark_id_not_appointed[0].id):
                    counter_all += 1

            if counter_all == len(student_records):
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)
class ListStudentsWith(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
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
        
        
       
        students = Students.objects.all()
        students_to_return = []
        
        for student in students:
            student_records = records.filter(student_id=student.id)

            if len(student_records) > 0:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listMenuCategories(request):
    return Response([   'Студенты с большим количеством пятерок', 
                        'Студенты с большим количеством четверок', 
                        'Студенты с большим количеством троек', 
                        'Студенты с большим количеством двоек', 
                        'Студенты с большим количеством оценок зачтено',
                        'Студенты с большим количеством оценок зачтено',
                        'Студенты с большим количеством неявок',
                        'Студенты со всеми оценками больше тройки', 
                        'Студенты со всеми оценками больше двойки', 
                        'Студенты с меньшим количеством троек', 
                        'Студенты с меньшим количеством двоек', 
                        'Студенты с одной тройкой', 
                        'Студенты с одной двойкой', 
                        'Студенты с одним незачетом', 
                        'Студенты с одним зачетом', 
                        'Студенты с одной неявкой', 
                        'Студенты только с пятерками', 
                        'Студенты только с четверками', 
                        'Студенты только с тройками', 
                        'Студенты только с двойками', 
                        'Студенты только с оценками зачтено', 
                        'Студенты только с оценками незачтено', 
                        'Студенты только с неявками', 
                        'Найти студентов по запросу', 
                        ])
