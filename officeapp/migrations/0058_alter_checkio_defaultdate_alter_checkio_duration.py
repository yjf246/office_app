# Generated by Django 4.2.4 on 2024-02-08 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0057_alter_checkio_defaultdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkio',
            name='defaultdate',
            field=models.DateTimeField(default='2024-02-08 11:45:47.009567'),
        ),
        migrations.AlterField(
            model_name='checkio',
            name='duration',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]