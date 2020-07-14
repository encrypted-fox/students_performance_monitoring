# Generated by Django 3.0.8 on 2020-07-12 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('departments', '0005_auto_20200712_1853'),
        ('university_structure', '0005_auto_20200712_1853'),
        ('people', '0005_auto_20200712_1847'),
        ('information', '0005_auto_20200712_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='control_type_id',
            field=models.ForeignKey(db_column='control_type_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='information.ControlTypes'),
        ),
        migrations.AlterField(
            model_name='records',
            name='group_id',
            field=models.ForeignKey(db_column='group_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='university_structure.Groups'),
        ),
        migrations.AlterField(
            model_name='records',
            name='mark_id',
            field=models.ForeignKey(db_column='mark_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='information.Marks'),
        ),
        migrations.AlterField(
            model_name='records',
            name='student_id',
            field=models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='people.Students'),
        ),
        migrations.AlterField(
            model_name='records',
            name='subject_id',
            field=models.ForeignKey(db_column='subject_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='departments.Subjects'),
        ),
        migrations.AlterField(
            model_name='records',
            name='teacher_id',
            field=models.ForeignKey(db_column='teacher_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='people.Teachers'),
        ),
        migrations.AlterField(
            model_name='records',
            name='term_id',
            field=models.ForeignKey(db_column='term_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='information.Terms'),
        ),
        migrations.AlterField(
            model_name='retakes',
            name='control_type_id',
            field=models.ForeignKey(db_column='control_type_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='information.ControlTypes'),
        ),
        migrations.AlterField(
            model_name='retakes',
            name='group_id',
            field=models.ForeignKey(db_column='group_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='university_structure.Groups'),
        ),
        migrations.AlterField(
            model_name='retakes',
            name='mark_id',
            field=models.ForeignKey(db_column='mark_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='information.Marks'),
        ),
        migrations.AlterField(
            model_name='retakes',
            name='student_id',
            field=models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='people.Students'),
        ),
        migrations.AlterField(
            model_name='retakes',
            name='subject_id',
            field=models.ForeignKey(db_column='subject_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='departments.Subjects'),
        ),
        migrations.AlterField(
            model_name='retakes',
            name='teacher_id',
            field=models.ForeignKey(db_column='teacher_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='people.Teachers'),
        ),
        migrations.AlterField(
            model_name='retakes',
            name='term_id',
            field=models.ForeignKey(db_column='term_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='information.Terms'),
        ),
        migrations.AlterField(
            model_name='terms',
            name='start_year_id',
            field=models.ForeignKey(db_column='start_year_id', on_delete=django.db.models.deletion.CASCADE,
                                    to='information.StartYears'),
        ),
    ]
