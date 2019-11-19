from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


class FacultiesViewSet(viewsets.ModelViewSet):
    queryset = Faculties.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FacultiesSerializer


class EducationalProgramsViewSet(viewsets.ModelViewSet):
    queryset = EducationalPrograms.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EducationalProgramsSerializer


class SpecializationsViewSet(viewsets.ModelViewSet):
    queryset = Specializations.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SpecializationsSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupsSerializer


class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DepartmentsSerializer


class SubjectsViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubjectsSerializer


class SubjectBlocksViewSet(viewsets.ModelViewSet):
    queryset = SubjectBlocks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubjectBlocksSerializer


class SubjectsSubjectBlocksViewSet(viewsets.ModelViewSet):
    queryset = SubjectsSubjectBlocks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubjectsSubjectBlocksSerializer
