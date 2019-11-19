from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


class Departments(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DepartmentsSerializer


class Subjects(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubjectsSerializer


class SubjectBlocks(viewsets.ModelViewSet):
    queryset = SubjectBlocks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubjectBlocksSerializer


class SubjectsSubjectBlocks(viewsets.ModelViewSet):
    queryset = SubjectsSubjectBlocks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubjectsSubjectBlocksSerializer
