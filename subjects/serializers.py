from rest_framework import serializers

from .models import *


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = "__all__"


class SubjectBlocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectBlocks
        fields = "__all__"


class SubjectsSubjectBlocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectsSubjectBlocks
        fields = "__all__"


class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = '__all__'
