# Generated by Django 3.0.8 on 2020-07-06 15:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('university_structure', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='educationalprograms',
            table='educational_programs',
        ),
        migrations.AlterModelTable(
            name='faculties',
            table='faculties',
        ),
        migrations.AlterModelTable(
            name='groups',
            table='groups',
        ),
        migrations.AlterModelTable(
            name='specializations',
            table='specializations',
        ),
    ]