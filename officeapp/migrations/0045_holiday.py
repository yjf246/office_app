# Generated by Django 4.2.4 on 2024-01-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0044_alter_checkio_check_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HolidayName', models.CharField(max_length=255)),
                ('HolidayDate', models.DateField()),
            ],
        ),
    ]
