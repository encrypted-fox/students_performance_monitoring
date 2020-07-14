# Generated by Django 3.0.8 on 2020-07-12 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('university_structure', '0003_auto_20200712_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalprograms',
            name='faculty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university_structure.Faculties'),
        ),
        migrations.AlterField(
            model_name='groups',
            name='specialization_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='university_structure.Specializations'),
        ),
        migrations.AlterField(
            model_name='specializations',
            name='educational_program_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='university_structure.EducationalPrograms'),
        ),
    ]
