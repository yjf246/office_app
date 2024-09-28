# Generated by Django 4.2.4 on 2024-02-08 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0054_task_keyword1_task_keyword2_task_keyword3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkio',
            name='duration',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='announcements',
            name='date',
            field=models.DateField(default='2024-02-08'),
        ),
        migrations.AlterField(
            model_name='checkio',
            name='defaultdate',
            field=models.DateTimeField(default='2024-02-08 11:24:17.096516'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startdate',
            field=models.DateField(default='2024-02-08'),
        ),
    ]
