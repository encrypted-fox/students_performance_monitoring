from rest_framework import viewsets, permissions

from .serializers import *


class FacultiesViewSet(viewsets.ModelViewSet):
    queryset = Faculties.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FacultiesSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = DepartmentsSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class SpecializationsViewSet(viewsets.ModelViewSet):
    queryset = Specializations.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = SpecializationsSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class EducationLevelsViewSet(viewsets.ModelViewSet):
    queryset = EducationLevels.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = EducationLevelsSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class EducationProgramsViewSet(viewsets.ModelViewSet):
    queryset = EducationPrograms.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = EducationProgramsSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = GroupsSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'
