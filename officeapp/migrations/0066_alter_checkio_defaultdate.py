# Generated by Django 4.2.9 on 2024-02-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0065_alter_checkio_defaultdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkio',
            name='defaultdate',
            field=models.DateTimeField(default='2024-02-21 14:59:05.345349'),
        ),
    ]
