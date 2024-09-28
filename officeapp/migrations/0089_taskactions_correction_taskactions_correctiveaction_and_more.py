# Generated by Django 5.0.2 on 2024-09-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0088_taskactions_markasdone_alter_checkio_defaultdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskactions',
            name='Correction',
            field=models.CharField(blank=True, default=' ', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='taskactions',
            name='CorrectiveAction',
            field=models.CharField(blank=True, default=' ', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='taskactions',
            name='Description',
            field=models.CharField(blank=True, default=' ', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='announcements',
            name='date',
            field=models.DateField(default='2024-09-05'),
        ),
        migrations.AlterField(
            model_name='checkio',
            name='defaultdate',
            field=models.DateTimeField(default='2024-09-05 12:21:04.538796'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startdate',
            field=models.DateField(default='2024-09-05'),
        ),
        migrations.AlterField(
            model_name='task',
            name='TaskAddedTime',
            field=models.DateField(default='2024-09-05'),
        ),
        migrations.AlterField(
            model_name='taskactions',
            name='RootCase',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='taskactions',
            name='TaskSLA',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
