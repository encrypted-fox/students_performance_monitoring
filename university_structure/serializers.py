from rest_framework import serializers
from .models import *


class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = "__all__"


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = "__all__"


class SpecializationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specializations
        fields = "__all__"


class EducationProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationPrograms
        fields = "__all__"


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = "__all__"
