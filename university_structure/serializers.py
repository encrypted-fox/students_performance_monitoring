from rest_framework import serializers
from .models import *


class FacultiesSerializer(serializers.ModelSerializer):
    model = Faculties
    fields = "__all__"


class EducationalProgramsSerializer(serializers.ModelSerializer):
    model = EducationalPrograms
    fields = "__all__"


class SpecializationsSerializer(serializers.ModelSerializer):
    model = Specializations
    fields = "__all__"


class GroupsSerializer(serializers.ModelSerializer):
    model = Groups
    fields = "__all__"


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
