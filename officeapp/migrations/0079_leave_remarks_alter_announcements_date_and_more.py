# Generated by Django 5.0.2 on 2024-02-26 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0078_remove_userprofile_emergencyphoneno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='Remarks',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='announcements',
            name='date',
            field=models.DateField(default='2024-02-26'),
        ),
        migrations.AlterField(
            model_name='checkio',
            name='defaultdate',
            field=models.DateTimeField(default='2024-02-26 11:01:40.148231'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startdate',
            field=models.DateField(default='2024-02-26'),
        ),
        migrations.AlterField(
            model_name='task',
            name='TaskAddedTime',
            field=models.DateField(default='2024-02-26'),
        ),
    ]