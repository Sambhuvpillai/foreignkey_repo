# Generated by Django 4.0.4 on 2022-05-04 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0004_course_studentdetails_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdetails',
            name='student_course',
        ),
    ]