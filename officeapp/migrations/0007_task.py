# Generated by Django 4.2.4 on 2024-01-12 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeapp', '0006_userprofile_is_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskName', models.CharField(max_length=255)),
                ('AasignedTo', models.TextField()),
                ('DueDate', models.DateField(blank=True, null=True)),
                ('Category', models.TextField(blank=True, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Checklist', models.TextField(blank=True, null=True)),
                ('Attachments', models.FileField(blank=True, null=True, upload_to='taskimages')),
            ],
        ),
    ]