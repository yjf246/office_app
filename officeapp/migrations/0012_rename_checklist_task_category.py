# Generated by Django 4.2.4 on 2024-01-13 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0011_remove_task_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Checklist',
            new_name='Category',
        ),
    ]
