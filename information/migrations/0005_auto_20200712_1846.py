# Generated by Django 3.0.8 on 2020-07-12 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('university_structure', '0004_auto_20200712_1846'),
        ('departments', '0004_auto_20200712_1846'),
        ('people', '0004_auto_20200712_1846'),
        ('information', '0004_auto_20200712_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='control_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.ControlTypes'),
        ),
        migrations.AlterField(
            model_name='records',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university_structure.Groups'),
        ),
        migrations.AlterField(
            model_name='records',
            name='mark_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.Marks'),
        ),
        migrations.AlterField(
            model_name='records',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Students'),
        ),
        migrations.AlterField(
            model_name='records',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Subjects'),
        ),
        migrations.AlterField(
            model_name='records',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Teachers'),
        ),
        migrations.AlterField(
            model_name='records',
            name='term_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.Terms'),
        ),
        migrations.AlterField(
            model_name='retakes',
            name='control_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.ControlTypes'),
        ),
        migrations.AlterField(
            model_name='retakes',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university_structure.Groups'),
        ),
        migrations.AlterField(
            model_name='retakes',
            name='mark_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.Marks'),
        ),
        migrations.AlterField(
            model_name='retakes',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Students'),
        ),
        migrations.AlterField(
            model_name='retakes',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Subjects'),
        ),
        migrations.AlterField(
            model_name='retakes',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Teachers'),
        ),
        migrations.AlterField(
            model_name='retakes',
            name='term_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.Terms'),
        ),
        migrations.AlterField(
            model_name='terms',
            name='start_year_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.StartYears'),
        ),
    ]