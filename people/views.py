from rest_framework import viewsets, permissions

from .serializers import *


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TeachersSerializer


class TeachersViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TeachersSerializer
