# Generated by Django 4.1 on 2022-11-08 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_standard_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='standard',
            name='subjects',
            field=models.ManyToManyField(related_name='subjects', to='school.subjects'),
        ),
    ]
