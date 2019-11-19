from django.db import models
from university_structure.models import Faculties, EducationalPrograms

# Create your models here.


class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculties, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=120, null=False)


class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculties, on_delete=models.CASCADE, null=False)
    educational_program_id = models.ForeignKey(EducationalPrograms, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=120, null=False)


class SubjectBlocks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=False)


class SubjectsSubjectBlocks(models.Model):
    id = models.AutoField(primary_key=True)
    subject_id = models.ManyToManyField(Subjects)
    subject_block_id = models.ManyToManyField(SubjectBlocks)