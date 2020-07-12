from rest_framework import viewsets, permissions

from .serializers import *


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
