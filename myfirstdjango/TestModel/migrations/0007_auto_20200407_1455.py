# Generated by Django 2.2.11 on 2020-04-07 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0006_auto_20200404_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cname',
            field=models.CharField(max_length=20),
        ),
    ]
