from rest_framework import serializers
from .models import *


class StudentsSerializer(serializers.ModelSerializer):
    model = Students
    fields = "__all__"


class TeachersSerializer(serializers.ModelSerializer):
    model = Teachers
    fields = "__all__"

