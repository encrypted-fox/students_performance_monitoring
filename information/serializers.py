from rest_framework import serializers

from .models import *


class StartYearsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartYears
        fields = '__all__'


class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = '__all__'


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'


class ControlTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlTypes
        fields = '__all__'


class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = '__all__'
