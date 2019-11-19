from django.db import models

# Create your models here.


class Faculties(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=False)


class EducationalPrograms(models.Model):
    id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculties, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=120, null=False)


class Specializations(models.Model):
    id = models.AutoField(primary_key=True)
    educational_program_id = models.ForeignKey(EducationalPrograms, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=120, null=False)


class Groups(models.Model):
    id = models.CharField(max_length=10, primary_key=True, null=False)
    specialization_id = models.ForeignKey(Specializations, on_delete=models.CASCADE, null=False)







