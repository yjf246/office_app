# Generated by Django 4.2.4 on 2024-01-10 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0003_alter_userprofile_birthdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicalform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
