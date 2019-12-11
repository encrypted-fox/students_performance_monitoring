from rest_framework import serializers
from .models import *


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = "__all__"

