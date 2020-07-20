from rest_framework import viewsets, permissions

from .serializers import *


class SubjectsViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubjectsSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class SubjectBlocksViewSet(viewsets.ModelViewSet):
    queryset = SubjectBlocks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubjectBlocksSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class SubjectsSubjectBlocksViewSet(viewsets.ModelViewSet):
    queryset = SubjectsSubjectBlocks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubjectsSubjectBlocksSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'


class RecordsViewSet(viewsets.ModelViewSet):
    queryset = Records.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RecordsSerializer
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = '__all__'
