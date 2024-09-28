# Generated by Django 5.0.2 on 2024-02-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0079_leave_remarks_alter_announcements_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mac_address',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='announcements',
            name='date',
            field=models.DateField(default='2024-02-28'),
        ),
        migrations.AlterField(
            model_name='checkio',
            name='defaultdate',
            field=models.DateTimeField(default='2024-02-28 11:54:17.395095'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startdate',
            field=models.DateField(default='2024-02-28'),
        ),
        migrations.AlterField(
            model_name='task',
            name='TaskAddedTime',
            field=models.DateField(default='2024-02-28'),
        ),
    ]
