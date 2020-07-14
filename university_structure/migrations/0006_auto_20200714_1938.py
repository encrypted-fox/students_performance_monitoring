# Generated by Django 3.0.8 on 2020-07-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('university_structure', '0005_auto_20200712_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='number',
            field=models.CharField(default=1, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='groups',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]