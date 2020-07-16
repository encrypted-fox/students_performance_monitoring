from django.db import models
from information.models import StartYears


# Create your models here.


class Faculties(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=False)

    class Meta:
        db_table = 'faculties'


class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculties, on_delete=models.CASCADE, null=False, db_column='faculty_id')
    name = models.CharField(max_length=120, null=False)

    class Meta:
        db_table = 'departments'


class Specializations(models.Model):
    id = models.AutoField(primary_key=True)
    faculty_id = models.ForeignKey(Faculties, on_delete=models.CASCADE, null=False,
                                   db_column='faculty_id')
    name = models.CharField(max_length=120, null=False)

    class Meta:
        db_table = 'specializations'


class EducationLevels(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=False)

    class Meta:
        db_table = 'education_levels'


class EducationPrograms(models.Model):
    id = models.AutoField(primary_key=True)
    specialization_id = models.ForeignKey(Specializations, on_delete=models.CASCADE, null=False,
                                          db_column='specialization_id')
    main_department_id = models.ForeignKey(Departments, on_delete=models.CASCADE, null=False,
                                           db_column='main_department_id')
    education_level_id = models.ForeignKey(EducationLevels, on_delete=models.CASCADE, null=False,
                                           db_column='education_level_id')
    start_year_id = models.ForeignKey(StartYears, on_delete=models.CASCADE, null=False, db_column='start_year_id')
    name = models.CharField(max_length=120, null=False)

    class Meta:
        db_table = 'education_programs'


class Groups(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=10, unique=True, null=False)
    education_program_id = models.ForeignKey(EducationPrograms, on_delete=models.CASCADE, null=False,
                                             db_column='education_program_id')

    class Meta:
        db_table = 'groups'
