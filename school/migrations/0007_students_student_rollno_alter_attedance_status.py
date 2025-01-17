# Generated by Django 4.1 on 2022-11-09 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_attedance_status_attedance_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='student_rollno',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attedance',
            name='status',
            field=models.CharField(choices=[('absent', 'Absent'), ('present', 'Present')], max_length=8),
        ),
    ]
