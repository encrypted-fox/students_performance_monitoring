from rest_framework import viewsets, permissions

from .serializers import *


class FacultiesViewSet(viewsets.ModelViewSet):
    queryset = Faculties.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FacultiesSerializer


class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DepartmentsSerializer


class SpecializationsViewSet(viewsets.ModelViewSet):
    queryset = Specializations.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SpecializationsSerializer


class EducationProgramsViewSet(viewsets.ModelViewSet):
    queryset = EducationPrograms.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EducationProgramsSerializer


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GroupsSerializer
