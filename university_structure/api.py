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

