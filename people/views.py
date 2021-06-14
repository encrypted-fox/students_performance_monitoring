from rest_framework import viewsets, permissions

from .serializers import *


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = StudentsSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class TeachersViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TeachersSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'
