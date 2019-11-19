from rest_framework import serializers
from .models import *


class DepartmentsSerializer(serializers.ModelSerializer):
    model = Departments
    fields = "__all__"


class SubjectsSerializer(serializers.ModelSerializer):
    model = Subjects
    fields = "__all__"


class SubjectBlocksSerializer(serializers.ModelSerializer):
    model = SubjectBlocks
    fields = "__all__"


class SubjectsSubjectBlocksSerializer(serializers.ModelSerializer):
    model = SubjectsSubjectBlocks
    fields = "__all__"
