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

