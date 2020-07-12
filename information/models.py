from django.db import models

from departments.models import Subjects
from people.models import Students, Teachers
from university_structure.models import Groups


# Create your models here.


class StartYears(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(null=False)

    class Meta:
        db_table = 'start_years'


class Terms(models.Model):
    id = models.AutoField(primary_key=True)
    start_year_id = models.ForeignKey(StartYears, on_delete=models.CASCADE, null=False, db_column='start_year_id')
    number = models.IntegerField(null=False)

    class Meta:
        db_table = 'terms'


class Marks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = 'marks'


class ControlTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = 'control_types'


class Records(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE, null=False, db_column='student_id')
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=False, db_column='subject_id')
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE, null=False, db_column='group_id')
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=False, db_column='teacher_id')
    term_id = models.ForeignKey(Terms, on_delete=models.CASCADE, null=False, db_column='term_id')
    control_type_id = models.ForeignKey(ControlTypes, on_delete=models.CASCADE, null=False, db_column='control_type_id')
    mark_id = models.ForeignKey(Marks, on_delete=models.CASCADE, null=False, db_column='mark_id')
    datetime = models.DateTimeField(null=False, default=None)
    retake_count = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = 'records'


class Retakes(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE, null=False, db_column='student_id')
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=False, db_column='subject_id')
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE, null=False, db_column='group_id')
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE, null=False, db_column='teacher_id')
    term_id = models.ForeignKey(Terms, on_delete=models.CASCADE, null=False, db_column='term_id')
    control_type_id = models.ForeignKey(ControlTypes, on_delete=models.CASCADE, null=False, db_column='control_type_id')
    mark_id = models.ForeignKey(Marks, on_delete=models.CASCADE, null=False, db_column='mark_id')
    datetime = models.DateTimeField(null=False, default=None)
    retake_count = models.SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = 'retakes'
