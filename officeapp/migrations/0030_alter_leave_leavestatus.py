# Generated by Django 4.2.4 on 2024-01-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0029_leave_leavestatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='leavestatus',
            field=models.CharField(blank=True, choices=[('PENDING', 'PENDING'), ('REJECTED', 'REJECTED'), ('APPROVED', 'APPROVED')], max_length=100, null=True),
        ),
    ]
