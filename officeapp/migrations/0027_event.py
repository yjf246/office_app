# Generated by Django 4.2.4 on 2024-01-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0026_policy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=255)),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
            ],
        ),
    ]
