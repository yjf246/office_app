# Generated by Django 4.2.4 on 2024-02-03 06:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0049_alter_announcements_date_alter_checkio_defaultdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='date',
            field=models.DateField(default='2024-02-03'),
        ),
        migrations.AlterField(
            model_name='checkio',
            name='defaultdate',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 3, 12, 14, 13, 210982)),
        ),
    ]
