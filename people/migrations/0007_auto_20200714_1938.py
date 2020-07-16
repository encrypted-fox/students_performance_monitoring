# Generated by Django 3.0.8 on 2020-07-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('people', '0006_remove_teachers_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='number',
            field=models.CharField(default=1, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='students',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
