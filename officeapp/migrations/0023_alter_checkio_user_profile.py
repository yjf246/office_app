# Generated by Django 4.2.4 on 2024-01-18 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0022_alter_userprofile_username_checkio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkio',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officeapp.userprofile'),
        ),
    ]
