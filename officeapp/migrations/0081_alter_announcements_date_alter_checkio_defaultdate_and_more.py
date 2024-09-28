# Generated by Django 5.0.2 on 2024-03-02 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0080_userprofile_mac_address_alter_announcements_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='date',
            field=models.DateField(default='2024-03-02'),
        ),
        migrations.AlterField(
            model_name='checkio',
            name='defaultdate',
            field=models.DateTimeField(default='2024-03-02 11:32:06.919170'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startdate',
            field=models.DateField(default='2024-03-02'),
        ),
        migrations.AlterField(
            model_name='task',
            name='TaskAddedTime',
            field=models.DateField(default='2024-03-02'),
        ),
        migrations.CreateModel(
            name='Activeusers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Active', models.BooleanField(default=False)),
                ('mac_address', models.CharField(blank=True, max_length=17, null=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officeapp.userprofile')),
            ],
        ),
    ]
