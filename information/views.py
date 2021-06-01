from rest_framework import viewsets, permissions, authentication, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from people.models import Students
from subjects.models import Records
from people.serializers import StudentsSerializer


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


class ListExcellentStudents(viewsets.ViewSet):

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

class ListGoodStudentsWithMore5(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        """
        marks = Marks.objects.all()

        mark_id_5 = marks.filter(name='5')
        mark_id_4 = marks.filter(name='4')
        mark_id_pass = marks.filter(name='Зачтено')

        records = Records.objects.all()

        if request.data.is_final:
            records = records.filter(is_final=request.data.is_final)
        
        if request.data.teacher_id:
            records = records.filter(teacher_id=request.data.teacher_id)
        
        if request.data.group_id:
            records = records.filter(group_id=request.data.group_id)
        
        if request.data.subject_id:
            records = records.filter(subject_id=request.data.subject_id)
        
        if request.data.subject_block_id:
            records = records.filter(subject_block_id=request.data.subject_block_id)

        if request.data.control_type_id:
            records = records.filter(control_type_id=request.data.control_type_id)

        if request.data.term_id:
            records = records.filter(term_id=request.data.term_id)

        if request.data.mark_id:
            records = records.filter(mark_id=request.data.mark_id)

        if request.data.retake_count:
            records = records.filter(retake_count=request.data.retake_count)
        
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
                
                if record.mark_id == mark_id_5[0].id:
                    counter_5 += 1
                    counter_all += 1

                elif record.mark_id == mark_id_4[0].id:
                    counter_4 += 1
                    counter_all += 1

                elif record.mark_id == mark_id_pass[0].id:
                    counter_all += 1

            if counter_all == len(student_records) and counter_4 < counter_5:
                students_to_return.append(student)
        
        serializer = StudentsSerializer(students_to_return, many=True)

        return Response(serializer.data)

class ListGoodStudentsWithMore4(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all with more 4s and good marks only.
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

class ListStudentsOnlyWithMoreThen3(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students without 3s and less.
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

class ListStudentsOnlyWithMoreThen2(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all tstudents that pass exams.
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

class ListStudentsWith2(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students with mark 2 or not pass, or not appointed.
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

class ListStudentsOnlyWith2(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students with only marks 2 or not pass, or not appointed.
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

class ListStudentsWith(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all students with the given mark.
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

class ListExcellentStudents(viewsets.ViewSet):

    def list(self, request):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
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




        # def list(self, request):
        # """
        # This view should return a list of all students with more 5s then 4s. In addition, there should be only good marks.
        # """
        # records = Records.objects.all()
        # if request.data.teacher_id:
        #     records = records.filter(teacher_id=request.data.teacher_id)
        # if request.data.group_id:
        #     records = records.filter(group_id=request.data.group_id)
        # if request.data.subject_id:
        #     records = records.filter(subject_id=request.data.subject_id)
        # if request.data.subject_block_id:
        #     records = records.filter(subject_block_id=request.data.subject_block_id)
        # if request.data.control_type_id:
        #     records = records.filter(control_type_id=request.data.control_type_id)
        # if request.data.term_id:
        #     records = records.filter(term_id=request.data.term_id)
        # if request.data.mark_id:
        #     records = records.filter(mark_id=request.data.mark_id)
        # if request.data.retake_count:
        #     records = records.filter(retake_count=request.data.retake_count)
        # else 
        #     records = Records.objects.all()
       
        # students = Students.objects.all()

        # mark_names = 

        # for student in students:
        #     student_records = records.filter(student_id=student.id)
        #     for record in student_records:
        #         if 