# Generated by Django 2.2.11 on 2020-04-04 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_course_sc_student_tc_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='swhere',
            field=models.CharField(max_length=30),
        ),
    ]
