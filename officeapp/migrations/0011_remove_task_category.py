# Generated by Django 4.2.4 on 2024-01-13 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0010_alter_task_taskaddedtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Category',
        ),
    ]
