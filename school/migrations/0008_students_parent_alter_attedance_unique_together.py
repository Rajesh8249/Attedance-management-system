# Generated by Django 4.1 on 2022-11-09 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_students_student_rollno_alter_attedance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='parent',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='attedance',
            unique_together={('student_name', 'subject_id', 'attendance_date')},
        ),
    ]