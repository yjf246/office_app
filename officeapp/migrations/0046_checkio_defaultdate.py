# Generated by Django 4.2.4 on 2024-01-31 10:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0045_holiday'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkio',
            name='defaultdate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 31, 16, 20, 43, 880247)),
        ),
    ]
