from rest_framework import serializers
from .models import *


class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = "__all__"


class EducationalProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalPrograms
        fields = "__all__"


class SpecializationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specializations
        fields = "__all__"


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = "__all__"

