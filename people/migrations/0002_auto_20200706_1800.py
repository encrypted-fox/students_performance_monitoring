# Generated by Django 3.0.8 on 2020-07-06 15:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='students',
            table='students',
        ),
        migrations.AlterModelTable(
            name='teachers',
            table='teachers',
        ),
    ]