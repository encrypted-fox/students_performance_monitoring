from django.db import models


# Create your models here.


class Faculties(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=False)

    class Meta:
        db_table = 'faculties'


class EducationalPrograms(models.Model):
    id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculties, on_delete=models.CASCADE, null=False, db_column='faculty_id')
    name = models.CharField(max_length=120, null=False)

    class Meta:
        db_table = 'educational_programs'


class Specializations(models.Model):
    id = models.AutoField(primary_key=True)
    educational_program_id = models.ForeignKey(EducationalPrograms, on_delete=models.CASCADE, null=False,
                                               db_column='educational_program_id')
    name = models.CharField(max_length=120, null=False)

    class Meta:
        db_table = 'specializations'


class Groups(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=10, unique=True, null=False)
    specialization_id = models.ForeignKey(Specializations, on_delete=models.CASCADE, null=False,
                                          db_column='specialization_id')

    class Meta:
        db_table = 'groups'
