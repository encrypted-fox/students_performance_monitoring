from rest_framework import serializers

from .models import *


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = "__all__"


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = "__all__"


class SubjectBlocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectBlocks
        fields = "__all__"
