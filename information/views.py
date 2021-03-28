from rest_framework import viewsets, permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from people.models import Students


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


class ListAllStudentsWithExcellentMarks(APIView):
    def get(self, request, format=None):
        students = [student for student in Students.objects.filter('average_rating'=5)]
        return Response(usernames)
