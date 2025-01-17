# Generated by Django 4.2.4 on 2024-02-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0053_remove_task_aasignedto_alter_checkio_defaultdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Keyword1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='Keyword2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='Keyword3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checkio',
            name='defaultdate',
            field=models.DateTimeField(default='2024-02-07 15:36:09.990591'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startdate',
            field=models.DateField(default='2024-02-07'),
        ),
    ]
