from django.db import models

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
