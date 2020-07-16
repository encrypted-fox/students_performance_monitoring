from django.db import models

from information.models import Terms, ControlTypes, Marks
from people.models import Students, Teachers
from university_structure.models import EducationPrograms, Departments, Groups


# Create your models here.

class SubjectBlocks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=False)

    class Meta:
        db_table = 'subject_blocks'


class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    education_program_id = models.ForeignKey(EducationPrograms, on_delete=models.CASCADE, null=False,
                                             db_column='education_program_id')
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE, null=False,
                                      db_column='department_id')
    name = models.CharField(max_length=120, null=False)

    class Meta:
        db_table = 'subjects'


class SubjectsSubjectBlocks(models.Model):
    id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=False, db_column='subject_id')
    subject_block_id = models.ForeignKey(SubjectBlocks, on_delete=models.CASCADE, null=False,
                                         db_column='subject_block_id')

    class Meta:
        db_table = 'subjects_subject_blocks'


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
