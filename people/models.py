from django.db import models

from university_structure.models import Groups, Departments


# Create your models here.


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=20, unique=True, null=False)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE, null=False, db_column='group_id')
    first_name = models.CharField(max_length=30, null=False)
    fathers_name = models.CharField(max_length=60, null=True, default=None)
    last_name = models.CharField(max_length=150, null=False)
    email = models.EmailField(null=True, default=None)
    average_rating = models.FloatField(null=False, default=None)
    update_date = models.DateTimeField(null=False, default=None)

    class Meta:
        db_table = 'students'


class Teachers(models.Model):
    id = models.AutoField(primary_key=True)
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE, null=False, db_column='department_id')
    first_name = models.CharField(max_length=30, null=False)
    fathers_name = models.CharField(max_length=60, null=True, default=None)
    last_name = models.CharField(max_length=150, null=False)
    email = models.EmailField(null=True, default=None)
    degree = models.CharField(max_length=150, null=True, default=None)

    class Meta:
        db_table = 'teachers'
