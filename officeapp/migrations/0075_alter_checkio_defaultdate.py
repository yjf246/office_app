# Generated by Django 4.2.9 on 2024-02-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0074_alter_checkio_defaultdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkio',
            name='defaultdate',
            field=models.DateTimeField(default='2024-02-21 15:25:54.933451'),
        ),
    ]
