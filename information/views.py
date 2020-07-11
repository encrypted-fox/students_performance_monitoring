from rest_framework import viewsets, permissions

from .serializers import *


class TermsViewSet(viewsets.ModelViewSet):
    queryset = Terms.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TermsSerializer


class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MarksSerializer


class ControlTypesViewSet(viewsets.ModelViewSet):
    queryset = ControlTypes.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ControlTypesSerializer


class RecordsViewSet(viewsets.ModelViewSet):
    queryset = Records.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RecordsSerializer


class RetakesViewSet(viewsets.ModelViewSet):
    queryset = Retakes.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RecordsSerializer
