from rest_framework import viewsets, permissions

from .serializers import *


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
    queryset = SubjectBlocks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubjectBlocksSerializer


class RecordsViewSet(viewsets.ModelViewSet):
    queryset = Records.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RecordsSerializer
